

const date = "2023-12-13T20:57:52.504106+06:00";

function dateFormatter(dateString) {
  const date = new Date(dateString);
  const month = getCurrentMonth(date);

  return `${date.getDate()} ${month}.`;
}

function getCurrentMonth(date) {
  const reflect = {
    1() {
      return "Қаң";
    },
    2() {
      return "Ақп";
    },
    3() {
      return "Нау";
    },
    4() {
      return "Сәу";
    },
    5() {
      return "Мам";
    },
    6() {
      return "Мау";
    },
    7() {
      return "Шіл";
    },
    8() {
      return "Там";
    },
    9() {
      return "Қыр";
    },
    10() {
      return "Қаз";
    },
    11() {
      return "Қар";
    },
    12() {
      return "Жел";
    },
  };

  // 月份从0开始，所以要加1
  const currentMonth = date.getMonth() + 1;
  return reflect[currentMonth]();
}

console.log(dateFormatter(date));
