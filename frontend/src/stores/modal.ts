// Types
import type { I_User } from "~/types/user";

// 大菠萝
import { defineStore } from "pinia";

export const defaultModalState = {
  loginReuiqredModal: {
    open: false,
    actionDescription: "",
    nextUrl: "/",
  },
};

export const useModalStore = defineStore("modal", {
  state: () => {
    return defaultModalState;
  },
});
