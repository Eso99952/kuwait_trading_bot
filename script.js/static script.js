async function startBot() {
  const response = await fetch('/start_bot', { method: 'POST' });
  const data = await response.json();
  alert(data.message);
}

async function stopBot() {
  const response = await fetch('/stop_bot', { method: 'POST' });
  const data = await response.json();
  alert(data.message);
}

async function generateReport() {
  const response = await fetch('/report');
  const data = await response.json();
  alert(data.message);
}

async function getMarketData() {
  const symbol = document.getElementById('symbol').value || 'KSE:ABK';
  const response = await fetch(`/get_market_data?symbol=${symbol}`);
  const data = await response.json();
  document.getElementById('marketData').innerText = JSON.stringify(data, null, 2);
}

async function depositPix() {
  const amount = parseFloat(document.getElementById('pixAmount').value) || 0;
  const response = await fetch('/deposit_pix', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ amount }),
  });
  const data = await response.json();
  alert(data.message);
}

async function withdrawPix() {
  const amount = parseFloat(document.getElementById('pixAmount').value) || 0;
  const response = await fetch('/withdraw_pix', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ amount }),
  });
  const data = await response.json();
  alert(data.message);
}
