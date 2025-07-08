function updateData() {
  fetch("https://growth-api-be3i.onrender.com/update?token=Chip2150", {
    method: "POST"
  })
  .then(res => res.json())
  .then(data => alert(data.message || "✅ 更新完成"))
  .catch(err => alert("❌ 更新失敗"));
}
