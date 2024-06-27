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
          <p>消息记录...</p>
        </div>
        <el-input
          type="textarea"
          v-model="message"
          placeholder="输入消息..."
          class="message-input">
        </el-input>
        <el-button type="primary" @click="sendMessage">发送</el-button>
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
        { name: '招聘小助手', avatar: '', lastMessage: '昨天的消息内容消息内容' },
        { name: '联系人 001', avatar: '', lastMessage: '今天的消息内容' },
        { name: '联系人 002', avatar: '', lastMessage: '前天的消息内容' }
      ],
      activeContact: { name: '联系人 001' }, // Example active contact
      currentUser: { name: '' },
      chatMessages: [] // 添加这行来初始化聊天消息数组
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log('Opened: ' + key);
    },
    handleClose(key, keyPath) {
      console.log('Closed: ' + key);
    },
    setActiveContact(contact) {
      this.activeContact = contact;
    },
    sendMessage() {
      if (!this.message.trim()) {
        // 如果消息为空,不发送
        return;
      }

      // 假设当前用户的用户名存储在 Vuex 中
      const senderUsername = this.currentUser.name;
      
      // 接收者是当前活跃的联系人
      const receiverUsername = this.activeContact.name;
      console.log(senderUsername)
      console.log(receiverUsername)

      // 准备发送给后端的数据
      const messageData = {
        sender_name: senderUsername,
        receiver_name: receiverUsername,
        content: this.message
      };

      // 发送 POST 请求到后端
      this.$axios.post('/api/create_message/', messageData)
        .then(response => {
          if (response.data.status === 'success') {
            console.log('Message sent successfully:', response.data);
            // 可以在这里更新UI,比如将消息添加到聊天记录中
            this.updateChatMessages({
              sender: senderUsername,
              content: this.message,
              timestamp: new Date(),
              id: response.data.message_id
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
    },

    // 新增方法来更新聊天记录
    updateChatMessages(newMessage) {
      // 这里你需要根据你的数据结构来实现
      // 例如,你可能需要将新消息添加到某个数组中
      if (!this.chatMessages) {
        this.chatMessages = [];
      }
      this.chatMessages.push(newMessage);
    },
    fetchPersonalInfo() {
      const username = this.$store.state.user.username;  // 从 Vuex 获取用户名
      this.$axios.get('/api/get_personal_info/', {
        params: {
          username: username  // 将用户名作为查询参数发送
        }
      })
      .then(response => {
        console.log('Personal Info:', response.data);
        this.currentUser.name = response.data.name;
      })
      .catch(error => {
        console.error('Failed to fetch personal info:', error);
      });
    },
    fetchAllPersonalInfo() {
      const username = '';  // 从 Vuex 获取用户名
      this.$axios.get('/api/get_personal_info_list/', {

      })
      .then(response => {
        console.log('Personal Info:', response.data);
        currentUser.name = response.data.name;
      })
      .catch(error => {
        console.error('Failed to fetch personal info:', error);
      });
    },

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
  height: 48.5vh;
  overflow-y: auto;
  padding: 20px;
  background: #fff;
  border: 1px solid #d3d3d3;
}

.message-input {
  margin-top: 20px;
  margin-bottom: 15px;
}
</style>