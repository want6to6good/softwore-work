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
    // console.log(this.$store.state.user)

    return {
      resumeData: {
        // id: this.$store.state.user.id,
        // Include initial data similar to ResumeMain for demonstration
        portrait: 'path/to/image.jpg',
        name: '小汪',
        sex: '男',
        education: '某大学计算机科学与技术学院，本科，2012 - 2016',
        experience: '软件开发工程师，某科技公司，2016至今。负责公司产品后端开发与维护。',
        skills: '熟练使用Java, Python, JavaScript等编程语言；掌握Spring, Django, Vue.js框架。',
        projects: '在线教育平台 - 主导后端开发和系统架构设计。',
        certifications: 'Oracle Certified Java Programmer, 2018',
        username: this.$store.state.user.username
      }
    }
  },
  methods: {
    submitChanges() {
      console.log(this.resumeData);
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
        console.log('Response:', response);
        this.$message.success('简历修改已提交成功!');
      })
      .catch(error => {
        console.error('Error:', error);
        this.$message.error('提交失败，请检查网络或联系管理员!');
      });
    },
    returnToMain() {
      this.$router.push({ name: 'ResumeMain' });
    }
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