import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

function getSafeSessionStorage(key) {
	console.log(sessionStorage)
	const item = sessionStorage.getItem(key);
	console.log(key, item)
  try {
    return item ? JSON.parse(item) : null;
  } catch (error) {
    console.error(`Error parsing sessionStorage item "${key}":`, error);
    return null;
  }
}

export default new Vuex.Store({
  state: {
    user: getSafeSessionStorage('user') || {},
    // student: getSafeSessionStorage('student') || {},
    Authorization: sessionStorage.getItem('Authorization') || '',
    // isPractice: sessionStorage.getItem('isPractice') || false
  },
  mutations: {
	  setUser(state, value) {
		state.user = value;
		sessionStorage.setItem("user", JSON.stringify(value));
	  },
	  setStudent(state, value) {
		  state.student = value;
		  sessionStorage.setItem("student", JSON.stringify(value));
	  },
	  setAuthorization(state, value) {
		  state.Authorization = value;
		  sessionStorage.setItem("Authorization", value);
	  },
	  setIsPractice(state, value) {
		  state.isPractice = value;
		  sessionStorage.setItem("isPractice", value)
	  }
  },
  actions: {
  },
  modules: {
  }
})
