function unsubscribe(userId) {
  fetch("/unsubscribe", {
    method: "POST",
    body: JSON.stringify({ userId: userId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
