<template>
  <div class="resume-main">
    <h1>简历中心</h1>
    <div class="resume-info">
      <el-avatar :src="resumeData.portrait" size="large"></el-avatar>
      <div><label>姓名：</label>{{ resumeData.name }}</div>
      <div><label>性别：</label>{{ resumeData.sex }}</div>
      <div><label>教育经历：</label>{{ resumeData.education }}</div>
      <div><label>工作经历：</label>{{ resumeData.experience }}</div>
      <div><label>技能：</label>{{ resumeData.skills }}</div>
      <div><label>项目经历：</label>{{ resumeData.projects }}</div>
      <div><label>认证和证书：</label>{{ resumeData.certifications }}</div>
    </div>
    <!-- 导航按钮 -->
    <el-row type="flex" justify="center" class="row-bg">
      <el-col :span="8">
        <el-button type="primary" @click="editResume">修改简历</el-button>
      </el-col>
    </el-row>
    <router-view :key="$route.path"></router-view> <!-- 添加 :key 来触发重新渲染 -->
  </div>
</template>

<script>
export default {
  name: 'ResumeMain',
  data() {
    return {
      resumeData: {
        portrait: 'path/to/image.jpg',
        name: '小汪',
        sex: '男',
        education: '某大学计算机科学与技术学院，本科，2012 - 2016',
        experience: '软件开发工程师，某科技公司，2016至今。负责公司产品后端开发与维护。',
        skills: '熟练使用Java, Python, JavaScript等编程语言；掌握Spring, Django, Vue.js框架。',
        projects: '在线教育平台 - 主导后端开发和系统架构设计。',
        certifications: 'Oracle Certified Java Programmer, 2018'
      }
    }
  },
  methods: {
    editResume() {
      this.$router.push({ name: 'ResumeView' });
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
        // this.resumeData = response.data; // 根据需要更新 resumeData
      })
      .catch(error => {
        console.error('Failed to fetch personal info:', error);
      });
    },
    fetchPersonalResume() {
      const username = this.$store.state.user.username;  // 从 Vuex 获取用户名
      this.$axios.get('/api/get_resume/', {
        params: {
          username: username  // 将用户名作为查询参数发送
        }
      })
      .then(response => {
        console.log('Personal Resume:', response.data);
        // this.resumeData = response.data; // 根据需要更新 resumeData
      })
      .catch(error => {
        console.error('Failed to fetch personal resume:', error);
      });
    }
  },
  mounted() {
    this.fetchPersonalInfo();
    this.fetchPersonalResume();
  }
}
</script>
<style scoped>
.resume-main {
  padding: 20px;
}

.row-bg {
    margin-top: 30px; /* 增加更多间距 */
  margin-bottom: 20px;
}

.resume-info div{
  margin-bottom: 5px;
  margin-top: 15px;
}

label {
  font-weight: bold;
  margin-right: 5px;
}
</style>