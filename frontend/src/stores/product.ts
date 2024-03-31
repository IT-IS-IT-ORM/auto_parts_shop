// Types
import type { I_Product } from "~/types/product";

// 大菠萝
import { defineStore } from "pinia";

// Utils
import _ from "lodash";

interface I_ProductStore {
  categoryList: I_Product["category"];
}

export const useProductStore = defineStore("product", {
  state: (): I_ProductStore => ({
    categoryList: [],
  }),
});
