
function updateData() {
  fetch("https://your-render-api.onrender.com/update?token=YOUR_SECRET_TOKEN", { method: "POST" })
    .then(res => res.json())
    .then(data => alert(data.message || "✅ 更新完成"))
    .catch(err => alert("❌ 更新失敗"));
}
