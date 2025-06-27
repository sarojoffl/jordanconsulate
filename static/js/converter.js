// Import NepaliDate as ES module from CDN
import NepaliDate from 'https://cdn.jsdelivr.net/npm/nepali-date-converter/dist/nepali-date-converter.es5.js';

// Currency conversion rate (update as needed)
const JOD_TO_NPR_RATE = 116.5;

// Currency Converter
document.getElementById('convertCurrencyBtn').addEventListener('click', () => {
  const amount = parseFloat(document.getElementById('amount').value);
  const direction = document.getElementById('direction').value;
  let result;

  if (isNaN(amount) || amount < 0) {
    alert('Please enter a valid amount');
    return;
  }

  if (direction === 'JOD_to_NPR') {
    result = amount * JOD_TO_NPR_RATE;
    document.getElementById('currencyResult').textContent = `${amount} JOD = ${result.toFixed(2)} NPR`;
  } else if (direction === 'NPR_to_JOD') {
    result = amount / JOD_TO_NPR_RATE;
    document.getElementById('currencyResult').textContent = `${amount} NPR = ${result.toFixed(2)} JOD`;
  } else {
    document.getElementById('currencyResult').textContent = 'Invalid conversion direction';
  }
});

// Date Converter
document.getElementById('convertDateBtn').addEventListener('click', () => {
  const inputDateStr = document.getElementById('gregorian_date').value;

  if (!inputDateStr) {
    alert('Please select a Gregorian date');
    return;
  }

  try {
    const [year, month, day] = inputDateStr.split('-').map(Number);
    const jsDate = new Date(year, month - 1, day);
    if (isNaN(jsDate.getTime())) throw new Error('Invalid Date');

    // Convert JS Date to NepaliDate
    const nepDate = NepaliDate.fromAD(jsDate);

    // Format Nepali Date, English output
    const formattedDate = nepDate.format('ddd, DD MMMM YYYY', 'en');

    document.getElementById('nepaliDateResult').textContent = `Nepali Date: ${formattedDate}`;
  } catch (error) {
    alert('Failed to convert date. Please check input.');
    console.error('Date conversion error:', error);
  }
});
