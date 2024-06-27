<template>
  <div class="question-detail" v-if="question">
    <h1>{{ question.title }}</h1>
    <div class="difficulty" :class="question.difficulty.toLowerCase()">
      {{ question.difficulty }}
    </div>
    <div class="description">
      <h2>题目描述</h2>
      <p>{{ question.description }}</p>
    </div>
    <div class="examples">
      <div v-for="(example, index) in question.examples" :key="index" class="example">
        <h3>示例 {{ index + 1 }}:</h3>
        <pre>{{ example }}</pre>
      </div>
    </div>
    <div class="code-editor">
      <h2>代码编辑器</h2>
      <textarea v-model="code" rows="10" placeholder="在这里编写你的Python代码"></textarea>
    </div>
      <el-button type="primary" @click="submitCode">提交代码</el-button>
      <div v-if="testResult" class="test-result">
        <h3>测试结果：</h3>
          <pre>{{ testResult.stdout }}</pre>
          <pre v-if="testResult.stderr" class="error">标准错误：{{ testResult.stderr }}</pre>
          <p :class="{ 'success': testResult.stdout == 'All test cases passed!\n', 'error': testResult.stdout != 'All test cases passed!\n' }">
            {{ testResult.stdout == 'All test cases passed!\n' ? '测试通过！' : '测试未通过。' }}

          </p>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'QuestionDetail',
  data() {
    return {
      question: null,
      code: '',
      testResult: null,
    }
  },
  methods: {
    async submitCode() {
      try {
        //console.log('Submitting code:', {
          //questionId: this.question.id,
          //code: this.code
        //});

        const response = await axios.post('/api/test-code/', {
          question_id: this.question.id,
          code: this.code
        });
        
        this.testResult = response.data;
        console.log(this.testResult.stdout)
      } catch (error) {
        console.error('提交代码时出错:', error);
        this.testResult = {
          stdout: '',
          stderr: '提交代码时出错，请稍后再试。',
          returncode: 1
        };
      }
    },
    async fetchQuestionData() {
      // 这里应该是一个 API 调用来获取题目数据
      // 为了演示，我们使用一个模拟的数据集
      const questions = {
        1: {
          id: 1,
          title: '两数之和',
          difficulty: 'Easy',
          description: '给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。',
          examples: [
            '输入：nums = [2,7,11,15], target = 9\n输出：[0,1]\n解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。',
            '输入：nums = [3,2,4], target = 6\n输出：[1,2]',
            '输入：nums = [3,3], target = 6\n输出：[0,1]'
          ]
        },
        2: {
          id: 2,
          title: '无重复字符的最长子串',
          difficulty: 'Medium',
          description: '给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。',
          examples: [
            '输入：s = "abcabcbb"\n输出：3\n解释：因为无重复字符的最长子串是 "abc"，所以其长度为 3。',
            '输入：s = "bbbbb"\n1输出：1\n解释：因为无重复字符的最长子串是 "b"，所以其长度为 1。',
            '输入：s = "pwwkew"\n输出：3\n解释：因为无重复字符的最长子串是 "wke"，所以其长度为 3。'
          ]
        }
      }
      
      const id = parseInt(this.$route.params.id)
      this.question = questions[id]
    }
  },
  created() {
    this.fetchQuestionData()
  },
  watch: {
    '$route.params.id': 'fetchQuestionData'
  }
}
</script>


<style scoped>
.question-detail {
  padding: 20px;
}

h1 {
  margin-bottom: 10px;
}

.difficulty {
  display: inline-block;
  padding: 5px 10px;
  border-radius: 5px;
  font-weight: bold;
  margin-bottom: 20px;
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

.description, .examples, .code-editor {
  margin-bottom: 20px;
}

.example {
  background-color: #f8f9fa;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.test-result {
  margin-top: 20px;
  padding: 10px;
  background-color: #f8f9fa;
  border-radius: 5px;
}

.test-result pre {
  white-space: pre-wrap;
  word-wrap: break-word;
}

.error {
  color: #d9534f;
}

.success {
  color: #5cb85c;
}

textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>