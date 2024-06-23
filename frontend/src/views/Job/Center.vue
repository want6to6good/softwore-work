<template>
    <div class="center">
        <el-form ref="centerForm" status-icon :model="centerForm" :rules="rules" label-width="80px">
            <h1>个人中心</h1>
            <el-form-item label="姓名" prop="name">
                <el-input v-model="centerForm.name" placeholder="请输入姓名"></el-input>
            </el-form-item>
            <el-form-item label="性别" prop="gender">
                <el-input v-model="centerForm.gender" placeholder="请输入性别"></el-input>
            </el-form-item>
            <el-form-item label="昵称" prop="nickname">
                <el-input v-model="centerForm.nickname" placeholder="请输入昵称"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="updateInfo('centerForm')">确认修改</el-button>
                <el-button @click="cancel">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>
<script>
export default {
    data() {
        return {
            centerForm: {
                name: null,
                gender: null,
                nickname: null,  // 新增昵称字段
                user: null
            },
            rules: {
                name: [
                    { required: true, message: '请输入姓名', trigger: 'blur' },
                    { min: 2, max: 10, message: '长度在 2 到 10 个字符', trigger: 'blur' }
                ],
                gender: [
                    { required: true, message: '请输入性别', trigger: 'blur' }
                ],
                nickname: [  // 新增昵称验证规则
                    { required: true, message: '请输入昵称', trigger: 'blur' },
                    { min: 2, max: 10, message: '昵称长度在 2 到 10 个字符', trigger: 'blur' }
                ]
            }
        }
    },
    methods: {
        updateInfo(formName) {
            this.$refs[formName].validate((valide) => {
                if (valide) {
                    this.$axios.patch(
                        `/api/students/${this.centerForm.id}/?format=json`,
                        this.centerForm
                    ).then(res => {
                        console.log(res)
                        if (res.status == 200) {
                            this.$message({
                                message: '更新个人信息成功',
                                type: 'success'
                            });
                            // 更新缓存
                            this.$store.commit("setStudent", this.centerForm)
                        } else {
                            this.$message({
                                message: '更新个人信息失败',
                                type: 'error'
                            });
                        }
                    }).catch(error => {
                        console.log(error)
                    })
                } else {
                    // 表单验证失败
                }
            });
        },
        cancel() {
            this.$router.push('/job')
        }
    },
    created() {
        this.centerForm = this.$store.state.user;
    }
}
</script>


<style lang="scss" scoped>
	#center {}

	.el-form {
		margin-left: 350px;
		width: 400px;
	}

	.el-select {
		width: 320px;
	}

	.el-input {}
</style>
