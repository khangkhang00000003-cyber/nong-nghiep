/* Nông Xanh – menu di động + giỏ hàng (lưu trình duyệt, gửi đơn qua Zalo) */
(function () {
  "use strict";
  var KEY = "nongxanh_cart_v1";
  var cfg = window.NX || {};
  var cart = [];

  function load() { try { cart = JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { cart = []; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(cart)); } catch (e) {} }
  function vnd(n) { return n.toLocaleString("vi-VN") + "đ"; }
  function total() { return cart.reduce(function (s, i) { return s + i.price * i.qty; }, 0); }
  function count() { return cart.reduce(function (s, i) { return s + i.qty; }, 0); }

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  function toast(msg) {
    var t = $(".toast"); if (!t) return;
    t.textContent = msg; t.classList.add("show");
    clearTimeout(toast.h); toast.h = setTimeout(function () { t.classList.remove("show"); }, 2200);
  }

  function render() {
    $$(".cart-count").forEach(function (el) { el.textContent = count(); });
    var list = $(".cart-items"), empty = $(".cart-empty"), foot = $(".drawer footer");
    if (!list) return;
    list.innerHTML = "";
    empty.hidden = cart.length > 0; foot.hidden = cart.length === 0;
    cart.forEach(function (it, idx) {
      var li = document.createElement("li"); li.className = "cart-item";
      li.innerHTML =
        '<img src="' + it.img + '" alt="" width="64" height="64">' +
        '<div><strong></strong><small>' + vnd(it.price) + '</small>' +
        '<div class="qty"><button type="button" data-act="dec" aria-label="Giảm số lượng">−</button>' +
        '<input value="' + it.qty + '" readonly aria-label="Số lượng">' +
        '<button type="button" data-act="inc" aria-label="Tăng số lượng">+</button></div></div>' +
        '<button type="button" data-act="del" class="close" aria-label="Xóa khỏi giỏ">×</button>';
      li.querySelector("strong").textContent = it.name;
      li.addEventListener("click", function (e) {
        var a = e.target.getAttribute && e.target.getAttribute("data-act"); if (!a) return;
        if (a === "inc") it.qty++;
        if (a === "dec") it.qty = Math.max(1, it.qty - 1);
        if (a === "del") cart.splice(idx, 1);
        save(); render();
      });
      list.appendChild(li);
    });
    var sum = total();
    $(".cart-total").textContent = vnd(sum);
    var free = cfg.freeShip || 500000;
    $(".ship-note").textContent = sum >= free
      ? "Đơn của bạn được miễn phí vận chuyển."
      : "Mua thêm " + vnd(free - sum) + " để được miễn phí vận chuyển.";
  }

  function add(btn) {
    var qtyInput = btn.closest(".buy-row") ? $(".qty input", btn.closest(".buy-row")) : null;
    var q = qtyInput ? Math.max(1, parseInt(qtyInput.value, 10) || 1) : 1;
    var id = btn.dataset.id, found = cart.filter(function (i) { return i.id === id; })[0];
    if (found) found.qty += q;
    else cart.push({ id: id, name: btn.dataset.name, price: +btn.dataset.price, img: btn.dataset.img, qty: q });
    save(); render(); toast("Đã thêm “" + btn.dataset.name + "” vào giỏ");
  }

  function orderText() {
    var lines = ["Chào Nông Xanh, mình muốn đặt hàng:"];
    cart.forEach(function (i, n) { lines.push((n + 1) + ". " + i.name + " x" + i.qty + " = " + vnd(i.price * i.qty)); });
    lines.push("Tạm tính: " + vnd(total()));
    lines.push("Họ tên, số điện thoại và địa chỉ nhận hàng của mình là: ");
    return lines.join("\n");
  }

  function openCart(open) { document.body.classList.toggle("cart-open", open); if (open) { var c = $(".drawer .close"); if (c) c.focus(); } }

  document.addEventListener("DOMContentLoaded", function () {
    load(); render();
    var mb = $(".menu-btn"), nav = $(".nav");
    if (mb) mb.addEventListener("click", function () { var o = nav.classList.toggle("open"); mb.setAttribute("aria-expanded", o); });
    $$(".add-to-cart").forEach(function (b) { b.addEventListener("click", function () { add(b); }); });
    $$(".qty").forEach(function (q) {
      if (q.closest(".cart-item")) return;
      var inp = $("input", q);
      $$("button", q).forEach(function (b) {
        b.addEventListener("click", function () {
          var v = parseInt(inp.value, 10) || 1;
          inp.value = b.dataset.act === "inc" ? Math.min(99, v + 1) : Math.max(1, v - 1);
        });
      });
    });
    $$(".cart-btn").forEach(function (b) { b.addEventListener("click", function () { openCart(true); }); });
    $$(".drawer .close, .drawer-back").forEach(function (b) { b.addEventListener("click", function () { openCart(false); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") openCart(false); });
    var send = $(".send-zalo");
    if (send) send.addEventListener("click", function () {
      var txt = orderText();
      var done = function () { toast("Đã sao chép đơn hàng. Hãy dán vào Zalo và gửi cho shop."); setTimeout(function () { window.open("https://zalo.me/" + cfg.zalo, "_blank", "noopener"); }, 700); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(done, done); else done();
    });
    var mail = $(".send-mail");
    if (mail) mail.addEventListener("click", function () {
      window.location.href = "mailto:" + cfg.email + "?subject=" + encodeURIComponent("Đặt hàng Nông Xanh") + "&body=" + encodeURIComponent(orderText());
    });
  });
})();
