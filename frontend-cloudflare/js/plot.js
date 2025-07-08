
fetch("data/growth.csv")
  .then(res => res.text())
  .then(csv => {
    const rows = csv.split('\n').map(r => r.split(','));
    const labels = rows[0].slice(2); // skip 代號, 名稱
    const traces = rows.slice(1).map(row => ({
      x: labels,
      y: row.slice(2).map(Number),
      type: 'scatter',
      name: row[1] + " (" + row[0] + ")"
    }));
    Plotly.newPlot("chart", traces, { title: "月營收年增率趨勢" });
  });
