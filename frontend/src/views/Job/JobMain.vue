<template>
	<div id="job">
		<el-row type="flex" justify="center">
			<el-col :span="4">
				<el-input v-model="key" placeholder="请输入职位名称" prefix-icon="el-icon-search" clearable></el-input>
			</el-col>
			<el-col :span="4">
				<el-button type="primary" @click="searchJob()">搜索职位</el-button>
			</el-col>
		</el-row>
		<el-row>
			<h1 style="border-left: solid 10px rgb(220, 208, 65);">职位列表</h1>
			<div style="padding-left: 15px">
				<el-col :span="4" v-for="(item, index) in pagination.results" :key="index" :offset="index > 0 ? 1 : 0">
					<el-card :body-style="{ padding: '0px' }" v-loading="loading">
						<!-- <img src="@/assets/job.png" class="image"> -->
						<div style="padding: 14px;">
							<span>{{ item.title }}</span>
							<p>
								<span>发布日期：{{ item.post_date }}</span>
								<br />
								<span>地点：{{ item.location }}</span>
							</p>
							<div class="bottom clearfix">
								<el-button type="text" class="button" @click="applyToJob(index)">报名</el-button>
							</div>
						</div>
					</el-card>
				</el-col>
			</div>
		</el-row>
		<Pagination :count="pagination.count" @size-change="handleSizeChange" @current-change="handleCurrentChange"></Pagination>
	</div>
</template>

<script>
import Pagination from '@/components/Pagination.vue'
export default {
	data() {
		return {
			loading: false,
			key: null,
			page: 1,
			page_size: 5,
			pagination: {
				count: null,
				next: null,
				previous: null,
				results: []
			}
		}
	},
	components: {
		Pagination
	},
	methods: {
		getJobInfo() {
			this.$axios(`/api/jobs/?format=json`, {
				params: {
					page: this.page,
					page_size: this.page_size,
					// student_id: this.$store.state.student.id,
				}
			}).then(res => {
				this.pagination = res.data
				this.loading = false
			}).catch(error => {
				console.log(error)
			})
		},
		handleSizeChange(val) {
			this.page_size = val
			this.searchJob()
		},
		handleCurrentChange(val) {
			this.page = val
			this.searchJob()
		},
		searchJob() {
			if (this.key) {
				this.$axios(`/api/jobs/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						search: this.key,
						student_id: this.$store.state.student.id,
					}
				}).then(res => {
					if (res.status == 200) {
						this.pagination = res.data
					}
				})
			} else {
				this.getJobInfo()
			}
		},
		applyToJob(index) {
			localStorage.removeItem('job');
			localStorage.setItem("job", JSON.stringify(this.pagination.results[index]));
			this.$router.push({
				path: '/Pay',
				query: {}
			})
		}
	},
	created() {
		this.getJobInfo()
		this.loading = true
	}
}
</script>

<style lang="scss" scoped>
    #job {
        margin-top: 10px;
        display: flex; // 设置为flex布局
        // align-items: center; // 子元素水平居中

        flex-direction: column; // 子元素垂直排列
    }
    
	.bottom {
		margin-top: 13px;
		line-height: 12px;
	}

	.button {
		padding: 0;
	}

	.image {
		width: 50%;
		height: 80%;
		display: block;
		margin: 20px auto 10px auto;
	}

	.clearfix:before,
	.clearfix:after {
		display: table;
		content: "";
	}

	.clearfix:after {
		clear: both;
	}
</style>