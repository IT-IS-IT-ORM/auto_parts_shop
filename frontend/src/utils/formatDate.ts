function getCurrentMonth(date: Date, fullversion: boolean) {
  const months = [
    ["қаң", "қаңтар"],
    ["ақп", "ақпан"],
    ["нау", "науырыз"],
    ["сәу", "сәуір"],
    ["мам", "мамыр"],
    ["мау", "маусым"],
    ["шіл", "шілде"],
    ["там", "тамыз"],
    ["қыр", "қыркүйек"],
    ["қаз", "қазан"],
    ["қар", "қараша"],
    ["жел", "желтоқсан"],
  ];

  const currentMonth = date.getMonth();
  return months[currentMonth][Number(fullversion)];
}

export default function dateFormatter(
  dateString: string,
  fullversion: boolean
) {
  const date = new Date(dateString);
  const monthStr = getCurrentMonth(date, fullversion);

  if (fullversion) {
    return `${date.getDate()} ${monthStr} ${date.getFullYear()}ж.`;
  }

  return `${date.getDate()} ${monthStr}.`;
}
