(function () {
  var HOTLINE = "0778123268";
  var ZALO = "https://zalo.me/0778123268";
  var TEL = "tel:0778123268";

  function blocked(url) {
    return /admin-ajax\.php/i.test(String(url || ""));
  }
  var origOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (method, url) {
    this.__stBlock = blocked(url);
    return origOpen.apply(this, arguments);
  };
  var origSend = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function () {
    if (this.__stBlock) {
      try { this.abort(); } catch (e) {}
      return;
    }
    return origSend.apply(this, arguments);
  };
  if (window.fetch) {
    var origFetch = window.fetch;
    window.fetch = function (input, init) {
      var url = typeof input === "string" ? input : (input && input.url) || "";
      if (blocked(url)) return Promise.resolve(new Response("", { status: 204 }));
      return origFetch.apply(this, arguments);
    };
  }

  function field(form, name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? String(el.value || "").trim() : "";
  }
  function phoneOk(value) {
    var d = value.replace(/[^\d+]/g, "");
    return /^(0\d{9}|84\d{9}|\+84\d{9})$/.test(d);
  }
  function show(form, ok, text) {
    var box = form.querySelector(".forminator-response-message");
    if (!box) {
      box = document.createElement("div");
      box.className = "forminator-response-message";
      box.setAttribute("role", "alert");
      form.insertBefore(box, form.firstChild);
    }
    box.classList.remove("forminator-error", "forminator-success", "st-on");
    box.classList.add("st-on", ok ? "forminator-success" : "forminator-error");
    box.setAttribute("aria-hidden", "false");
    box.innerHTML = text;
  }
  function handle(form) {
    if (form.getAttribute("data-st-sent") === "1") return;
    var name = field(form, "name-1");
    var phone = field(form, "phone-1");
    var email = field(form, "email-1");
    var city = field(form, "select-2");
    var area = field(form, "select-1");
    var model = field(form, "select-3") || field(form, "select-4");
    var errors = [];
    if (name.length < 2) errors.push("Nhập họ và tên.");
    if (!phoneOk(phone)) errors.push("Số điện thoại chưa đúng (10 số, bắt đầu bằng 0).");
    var emailEl = form.querySelector('[name="email-1"]');
    if (emailEl && emailEl.getAttribute("data-required") && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      errors.push("Email chưa đúng.");
    }
    var cityEl = form.querySelector('[name="select-2"]');
    if (cityEl && cityEl.getAttribute("data-required") && !city) errors.push("Chọn thành phố.");
    if (errors.length) {
      show(form, false, errors.join("<br>"));
      return;
    }
    var lines = [
      "Sài Thành Group — đăng ký lái thử / liên hệ",
      "Họ tên: " + name,
      "SĐT: " + phone
    ];
    if (email) lines.push("Email: " + email);
    if (city) lines.push("Thành phố: " + city);
    if (area) lines.push("Khu vực: " + area);
    if (model) lines.push("Mẫu xe: " + model);
    var info = lines.join("\n");
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(info).catch(function () {});
    }
    form.setAttribute("data-st-sent", "1");
    var actions =
      '<div class="st-lead-actions">' +
      '<a href="' + TEL + '">Gọi 0778 123 268</a>' +
      '<a href="' + ZALO + '" target="_blank" rel="noopener">Nhắn Zalo</a>' +
      "</div>";
    show(
      form,
      true,
      "Đã ghi nhận thông tin. Sài Thành CN1 sẽ liên hệ với bạn." +
      "<br>Nội dung đã được sao chép — dán vào Zalo nếu ô chat đang trống." +
      actions
    );
    var zalo = window.open(ZALO, "_blank", "noopener");
    var tel = document.createElement("a");
    tel.href = TEL;
    tel.style.display = "none";
    document.body.appendChild(tel);
    tel.click();
    tel.remove();
    if (!zalo) {
      /* popup blocked; the buttons above still work */
    }
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest(".forminator-button-submit, button[type='submit']");
    if (!btn) return;
    var form = btn.closest("form");
    if (!form || !form.classList.contains("forminator-custom-form")) return;
    e.preventDefault();
    e.stopPropagation();
    handle(form);
  }, true);

  document.addEventListener("submit", function (e) {
    var form = e.target;
    if (!form || !form.classList || !form.classList.contains("forminator-custom-form")) return;
    e.preventDefault();
    e.stopPropagation();
    handle(form);
  }, true);

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form.forminator-custom-form").forEach(function (form) {
      form.setAttribute("action", "/lai-thu");
      form.setAttribute("method", "get");
      form.addEventListener("submit", function (e) {
        e.preventDefault();
      });
    });
  });
})();
