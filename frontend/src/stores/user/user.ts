// Types
import type { I_User } from "~/types/user";

// 大菠萝
import { defineStore } from "pinia";

// Utils
import _ from "lodash";

export const defaultUserState: I_User = {
  id: -1,
  role: role.guest,
  phone: "",
  fullname: "",
  createTime: "",
  token: "",
};

export const useUser = defineStore("user", {
  state: () => {
    return defaultUserState;
  },

  actions: {
    initUserFromLocal() {
      const user = localStorage.get("user", defaultUserState) as I_User;

      if (!_.isEqual(user, defaultUserState)) {
        this.$state = user;
      }
    },

    logout() {
      localStorage.set("user", defaultUserState);
      this.$state = defaultUserState;
    },
  },

  getters: {
    isAuthenticated({ token }) {
      return token !== "";
    },
  },
});
