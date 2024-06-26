<template>
  <div class="resume-view">
    <h1>修改简历</h1>
    <el-form ref="resumeForm" :model="resumeData" label-position="right" label-width="100px">
      <el-form-item label="姓名">
        <el-input v-model="resumeData.name"></el-input>
      </el-form-item>
      <el-form-item label="性别">
        <el-input v-model="resumeData.sex"></el-input>
      </el-form-item>
      <el-form-item label="教育经历">
        <el-input v-model="resumeData.education" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="工作经历">
        <el-input v-model="resumeData.experience" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="技能">
        <el-input v-model="resumeData.skills" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="项目经历">
        <el-input v-model="resumeData.projects" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="认证和证书">
        <el-input v-model="resumeData.certifications" type="textarea"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitChanges">提交修改</el-button>
        <el-button @click="returnToMain">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'ResumeView',
  data() {
    return {
      resumeData: {
        portrait: 'path/to/image.jpg',
        name: '',
        sex: '',
        education: '',
        experience: '',
        skills: '',
        projects: '',
        certifications: '',
        username: this.$store.state.user.username
      }
    }
  },
  methods: {
    submitChanges() {
      // console.log(this.resumeData);
      // Ensure the API endpoint URL is correct and includes trailing slash
      this.$axios({
        url: '/api/change_resume/',
        method: 'post',
        data: {
          name: this.resumeData.name,
          sex: this.resumeData.sex,
          education: this.resumeData.education,
          experience: this.resumeData.experience,
          skills: this.resumeData.skills,
          projects: this.resumeData.projects,
          certifications: this.resumeData.certifications,
          username: this.resumeData.username  // Make sure the backend is expecting a 'username' field
        }
      })
      .then(response => {
        // console.log('Response:', response);
        this.$message.success('简历修改已提交成功!');
      })
      .catch(error => {
        console.error('Error:', error);
        this.$message.error('提交失败，请检查网络或联系管理员!');
      });
    },
    returnToMain() {
      this.$router.push({ name: 'ResumeMain' });
    }, 
        fetchPersonalInfo() {
      const username = this.$store.state.user.username;  // 从 Vuex 获取用户名
      this.$axios.get('/api/get_personal_info/', {
        params: {
          username: username  // 将用户名作为查询参数发送
        }
      })
      .then(response => {
        // console.log('Personal Info:', response.data);
        this.resumeData.name = response.data.name;
        this.resumeData.sex = response.data.gender === 'm' ? '男' : '女';
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
        console.log('Personal Resume:', response.data[0]);
        this.resumeData.education = response.data[0].education;
        this.resumeData.experience = response.data[0].experience;
        this.resumeData.skills = response.data[0].skills;
        this.resumeData.projects = response.data[0].projects;
        this.resumeData.certifications = response.data[0].certifications;
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
.resume-view {
  padding: 20px;
}


.el-form-item {
  margin-top: 30px; /* 增加表单项之间的间距 */
}

.el-input textarea {
  width: 100%;
}

.el-button {
  margin-top: 0px; /* 增加按钮与上方表单的间距 */
}
</style>