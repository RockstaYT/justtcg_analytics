/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      screens: {
        //sm: "0px",
        //md: "500px",
        //lg: "992px",
        // => @media (min-width: 992px) { ... }
      },
    },
  },
  plugins: [],
};
