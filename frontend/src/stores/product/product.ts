// Types
import type { I_Product, I_Category, I_SubCategory } from "~/types/product";

// 大菠萝
import { defineStore } from "pinia";

// Utils
import _ from "lodash";

export const useProduct = defineStore("product", {
  state: () => {
    return {
      categoryList: [],
      productList: [],
    };
  },
});
