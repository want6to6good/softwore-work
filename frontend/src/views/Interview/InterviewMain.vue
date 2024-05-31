<template>
  <div class="interview-main">
    <el-row> <!-- 增大间隙 -->
      <el-col :span="8" v-for="(item, index) in languages" :key="index">
        <el-card :body-style="{ padding: '20px' }">
          <div style="display: flex; align-items: center;">
            <img :src="item.imgSrc" alt="logo" style="width: 50px; height: 50px; margin-right: 15px;">
            <h3>{{ item.name }}</h3>
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
        { name: 'C/C++', imgSrc: '../../assets/language/c_cpp.png' },
        { name: 'Python', imgSrc: '../../assets/language/python.png' },
        { name: 'PHP', imgSrc: '../../assets/language/php.png' },
        { name: 'Java', imgSrc: '../../assets/language/java.png' },
        { name: 'JavaScript', imgSrc: '../../assets/language/javascript.png' },
        { name: 'Ruby', imgSrc: '../../assets/language/ruby.png' }
      ]
    };
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