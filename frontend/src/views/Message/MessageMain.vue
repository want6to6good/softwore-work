<template>
  <el-container class="message-main" style="height: 79vh;">
    <el-aside width="270px" style="background-color: #f2f2f2;">
      <el-menu default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
        <el-menu-item 
          v-for="(contact, index) in contacts" 
          :key="index" 
          :index="index.toString()" 
          @click="setActiveContact(contact)">
          <el-row align="middle">
            <el-col :span="6">
              <el-avatar :src="contact.avatar || 'default-avatar.png'"></el-avatar>
            </el-col>
            <el-col :span="18">
              <div class="name-message-container">
                <div class="contact-name">{{ contact.name }}</div>
                <div class="last-message">{{ contact.lastMessage }}</div>
              </div>
            </el-col>
          </el-row>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <el-main>
        <div class="chat-header">
          <span>{{ activeContact.name }}</span>
        </div>
        <div class="chat-messages">
          <div v-for="message in displayedMessages" :key="message.id" :class="['message', message.sender === currentUser.username ? 'sent' : 'received']">
            <p>{{ message.content }}</p>
            <span class="timestamp">{{ formatTimestamp(message.timestamp) }}</span>
          </div>
        </div>
        <el-input
          type="textarea"
          v-model="message"
          :disabled="!isContactSelected"
          placeholder="输入消息..."
          class="message-input">
        </el-input>
        <el-button type="primary" @click="sendMessage" :disabled="!isContactSelected">发送</el-button>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  name: 'MessageMain',
  data() {
    return {
      message: '',
      contacts: [
      ],
      activeContact: { name: '请选择联系人', username: '' }, // Example active contact
      currentUser: { name: '', username: '' },
      chatMessages: [] // 添加这行来初始化聊天消息数组
    };
  },

  computed: {
    displayedMessages() {
      return this.chatMessages.slice(0, 10);
    },
    
    isContactSelected() {
      return this.activeContact.username !== '';
    }
  },

  methods: {
    handleOpen(key, keyPath) {
      console.log('Opened: ' + key);
    },
    handleClose(key, keyPath) {
      console.log('Closed: ' + key);
    },
    sendMessage() {
      if (!this.message.trim()) {
        // 如果消息为空,不发送
        alert("不能发送空消息。");
        return;
      }

      const senderUsername = this.currentUser.username;
      const receiverUsername = this.activeContact.username;
      const messageData = {
        sender_name: senderUsername,
        receiver_name: receiverUsername,
        content: this.message
      };

      console.log(messageData);

      // 发送 POST 请求到后端
      this.$axios({
        method: 'post',
        url: '/api/create_message/',
        data: messageData
      }).then(response => {
          if (response.data.status === 'success') {
            console.log('Message sent successfully:', response.data);
            // 可以在这里更新UI,比如将消息添加到聊天记录中
            this.updateChatMessages({
               id: response.data.message_id,
               sender: this.currentUser.username,
               receiver: this.activeContact.username,
               content: this.message,
               timestamp: new Date().toISOString(),
               is_read: false
            });
            // 清空输入框
            this.message = '';
          } else {
            console.error('Failed to send message');
          }
        })
        .catch(error => {
          console.error('Error sending message:', error);
        });

      console.log('Chat Messages:', this.chatMessages);
    },

    // 新增方法来更新聊天记录
    updateChatMessages(newMessage) {
      this.chatMessages.unshift(newMessage);
      this.chatMessages = this.chatMessages.slice(0, 10);
    },

    fetchChatMessages() {
      // 获取别人给自己发过来的消息
      console.log(this.currentUser.username);
      this.$axios.get('/api/get_messages/', {
        params: {
          username: this.currentUser.username,
        }
      })
      .then(response => {
        console.log('Chat Messages:', response.data.messages);
        // this.chatMessages = response.data;
        this.chatMessages = response.data.messages.slice(0, 10);
        console.log(this.chatMessages);
      })
      .catch(error => {
        console.error('Failed to fetch chat messages:', error);
      });
    },


    fetchPersonalInfo() {
      const username = this.$store.state.user.username;  // 从 Vuex 获取用户名
      this.$axios.get('/api/get_personal_info/', {
        params: {
          username: username  // 将用户名作为查询参数发送
        }
      })
      .then(response => {
        //console.log('Personal Info:', response.data);
        this.currentUser.name = response.data.name;
        this.currentUser.username = response.data.user_name;
        //console.log(this.currentUser);
      })
      .catch(error => {
        console.error('Failed to fetch personal info:', error);
      });
    },

    fetchAllPersonalInfo() {
      this.$axios.get('/api/get_personal_info_list/')
        .then(response => {
          // console.log('All Personal Info:', response.data);
          // 将获取的数据转换为contacts数组的格式
          this.contacts = response.data
            .filter(user => user.user_name !== this.currentUser.username)
            .map(user => ({
              name: user.name,
              username: user.user_name,
              avatar: '', // 如果有头像信息，可以在这里添加
              lastMessage: '' // 如果有最后一条消息，可以在这里添加
          }));
        })
        .catch(error => {
          console.error('Failed to fetch all personal info:', error);
        });
    },

    setActiveContact(contact) {
      this.activeContact = {
        name: contact.name,
        username: contact.username
      };
      this.fetchChatMessages(); // 获取新联系人的聊天记录
      console.log(this.activeContact);
    },

    formatTimestamp(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleString();
    }
  },

  
  mounted() {
    this.fetchPersonalInfo();
    this.fetchAllPersonalInfo();
  }
}


</script>
<style scoped>
.message-main {
  border: 2px solid #d3d3d3; /* 设置边框 */
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); /* 可选: 添加轻微的阴影效果 */
}

.name-message-container {
  display: flex;
  justify-content: center;
  width: 100%;  /* 限制最大宽度，防止溢出 */
}

.contact-name {
  min-width: 0; /* 防止溢出导致的布局问题 */
  white-space: nowrap; /* 保持姓名在一行显示 */
  overflow: hidden; /* 隐藏溢出的内容 */
  text-overflow: ellipsis; /* 使用省略号表示溢出的文本 */
  flex-shrink: 0; /* 防止名称部分因为溢出而缩小 */
  margin-right: 10px; /* 添加右边距，与消息文本分开 */
}

.last-message {
  flex-grow: 1; /* 允许消息文本占用剩余空间 */
  overflow: hidden; /* 隐藏溢出的内容 */
  text-overflow: ellipsis; /* 使用省略号 */
  font-size: 12px;
  color: gray;
  text-align: left; /* 确保文本始终从左侧开始 */
}
.el-aside {
  border-right: 1px solid #d3d3d3;
}

.chat-header {
  padding: 10px 20px;
  border-bottom: 2px solid #ebebeb;
  font-size: 16px;
  font-weight: bold;
}
.chat-messages {
  height: 450px;
  overflow-y: auto;
  display: flex;
  flex-direction: column-reverse;
}

.message {
  margin: 5px 0;  /* 减小上下边距 */
  padding: 8px;   /* 减小内边距 */
  border-radius: 8px;
  max-width: 70%;
  font-size: 14px; /* 减小字体大小 */
  line-height: 1.2; /* 调整行高 */
}

.message p {
  margin: 0 0 5px 0; /* 减小段落底部边距 */
}

.sent {
  align-self: flex-end;
  background-color: #dcf8c6;
}

.received {
  align-self: flex-start;
  background-color: #fff;
}
.timestamp {
  font-size: 0.7em; /* 减小时间戳字体大小 */
  color: #888;
  display: block;   /* 使时间戳占据单独的一行 */
  text-align: right;
}
.message-input {
  margin-top: 20px;
  margin-bottom: 15px;
}
</style>