// Types
import type { I_Product, I_Category, I_SubCategory } from "~/types/product";

// 大菠萝
import { defineStore } from "pinia";

// Utils
import _ from "lodash";

export const useProduct = defineStore("product", {
  state: () => {
    return {
      categoryList: [
        {
          id: 1,
          title: "Tesla",
          isSelected: false,
          isCollapsed: false,
          subCategories: [
            {
              id: 2,
              title: "Model 1",
              isSelected: false,
            },
            {
              id: 3,
              title: "Model 2",
              isSelected: false,
            },
            {
              id: 4,
              title: "Model 3",
              isSelected: false,
            },
            {
              id: 5,
              title: "Model X",
              isSelected: false,
            },
            {
              id: 6,
              title: "Model Y",
              isSelected: false,
            },
            {
              id: 7,
              title: "Model Z",
              isSelected: false,
            },
          ],
        },
        {
          id: 8,
          title: "BMW",
          isSelected: false,
          isCollapsed: false,
          subCategories: [
            {
              id: 9,
              title: "X1",
              isSelected: false,
            },
            {
              id: 10,
              title: "X2",
              isSelected: false,
            },
            {
              id: 11,
              title: "X3",
              isSelected: false,
            },
            {
              id: 12,
              title: "m1",
              isSelected: false,
            },
            {
              id: 13,
              title: "m2",
              isSelected: false,
            },
          ],
        },
        {
          id: 14,
          title: "Toyota",
          isSelected: false,
          isCollapsed: false,
          subCategories: [
            {
              id: 15,
              title: "Camry",
              isSelected: false,
            },
            {
              id: 16,
              title: "Prius",
              isSelected: false,
            },
            {
              id: 17,
              title: "Corolla",
              isSelected: false,
            },
            {
              id: 18,
              title: "trucks",
              isSelected: false,
            },
          ],
        },
        {
          id: 19,
          title: "Nissan",
          isSelected: false,
          isCollapsed: false,
          subCategories: [
            {
              id: 20,
              title: "Altima",
              isSelected: false,
            },
            {
              id: 21,
              title: "buses",
              isSelected: false,
            },
            {
              id: 22,
              title: "trucks",
              isSelected: false,
            },
            {
              id: 23,
              title: "Jonga",
              isSelected: false,
            },
          ],
        },
      ],
      productList: [],
    };
  },
});
