<template>
  <div class="interview-main">
    <el-row>
      <!-- Python -->
      <el-col :span="8">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img src="@/assets/language/python.png" alt="Python logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>Python</h3>
          </div>
        </el-card>
      </el-col>
      <!-- C/C++ -->
      <el-col :span="8">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img src="@/assets/language/c++.png" alt="C++ logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>C/C++</h3>
          </div>
        </el-card>
      </el-col>
      <!-- Vue3 -->
      <el-col :span="8">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img src="@/assets/language/vue3.png" alt="Vue3 logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>Vue3</h3>
          </div>
        </el-card>
      </el-col>
      <!-- Java -->
      <el-col :span="8">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img src="@/assets/language/java.png" alt="Java logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>Java</h3>
          </div>
        </el-card>
      </el-col>
      <!-- JavaScript -->
      <el-col :span="8">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img src="@/assets/language/javascript.png" alt="JavaScript logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>JavaScript</h3>
          </div>
        </el-card>
      </el-col>
      <!-- Ruby -->
      <el-col :span="8">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img src="@/assets/language/ruby.png" alt="Ruby logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>Ruby</h3>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'InterviewMain',
  data() {
    return {
      languages: [
        { name: 'Python', imgSrc: '@/assets/language/python.png' },
        { name: 'C++', imgSrc: '@/assets/language/cpp.png' },
        { name: 'Vue3', imgSrc: '@/assets/language/vue3.png' },
        { name: 'Java', imgSrc: '@/assets/language/java.png' },
        { name: 'JavaScript', imgSrc: '@/assets/language/javascript.png' },
        { name: 'Ruby', imgSrc: '@/assets/language/ruby.png' }
      ]
    };
  },
  mounted() {
    this.languages.forEach(language => {
      console.log(`Loading image for ${language.name}: ${language.imgSrc}`);
    });
  }
}
</script>

<style scoped>
.interview-main {
  padding: 20px;
}
.el-card {
  cursor: pointer;
  transition: transform 0.3s ease;
  margin-bottom: 20px; /* 增加卡片之间的垂直间距 */
  margin-left: 20px;
}
.el-card:hover {
  transform: translateY(-5px);
}
</style>