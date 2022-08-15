import { createRouter } from "./context";
import { z } from "zod";
import { testfunction } from "../cardmarket/price-guide";

export const cardmarketRouter = createRouter().query("priceguide", {
  async resolve({ ctx }) {
    return await testfunction();
  },
});
