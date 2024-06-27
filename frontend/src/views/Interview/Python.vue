<template>
  <div class="python-page">
    <h1>Python 题库</h1>
    <div class="question-list">
      <div v-for="(question, index) in questions" :key="index" class="question-item" @click="goToQuestion(question.id)">
        <span class="question-number">{{ index + 1 }}</span>
        <span class="question-title">{{ question.title }}</span>
        <span class="question-difficulty" :class="question.difficulty.toLowerCase()">
          {{ question.difficulty }}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PythonPage',
  data() {
    return {
      questions: [
        { id: 1, title: '两数之和', difficulty: 'Easy' },
        { id: 2, title: '无重复字符的最长子串', difficulty: 'Medium' },
        { id: 3, title: '寻找两个正序数组的中位数', difficulty: 'Hard' },
        { id: 4, title: '最长回文子串', difficulty: 'Medium' },
        { id: 5, title: 'Z 字形变换', difficulty: 'Medium' },
        // 添加更多题目...
      ]
    }
  },
    methods: {
    goToQuestion(questionId) {
        this.$router.push({ name: 'QuestionDetail', params: { id: questionId } })
    }
    }
}
</script>

<style scoped>
.python-page {
  padding: 20px;
}

h1 {
  color: #333;
  margin-bottom: 20px;
}

.question-list {
  display: flex;
  flex-direction: column;
}

.question-item {
  display: flex;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #eee;
  cursor: pointer;
}

.question-item:hover {
  background-color: #f5f5f5;
}

.question-number {
  width: 30px;
  font-weight: bold;
}

.question-title {
  flex-grow: 1;
}

.question-difficulty {
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 12px;
}

.easy {
  background-color: #5cb85c;
  color: white;
}

.medium {
  background-color: #f0ad4e;
  color: white;
}

.hard {
  background-color: #d9534f;
  color: white;
}
</style>