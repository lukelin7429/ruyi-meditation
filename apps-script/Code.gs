/**
 * Ru-Yi English School 報名表後端（取代 sheet.best，免費）
 *
 * 重要：這支必須部署在 Ru-Yi 自己的 Google 帳號、綁 Ru-Yi 自己的試算表，
 *       與 MCC/人師的後端完全分離，絕不共用。
 *
 * 安裝：在 Ru-Yi 的報名試算表裡開 擴充功能 > Apps Script，
 *       把這份全部貼進去，存檔，再 部署 > 新增部署作業 > 網頁應用程式。
 *   - 執行身分 (Execute as)：我 (Me)
 *   - 誰可以存取 (Who has access)：所有人 (Anyone)
 * 部署後會拿到一個 /exec 結尾的網址，貼回 enroll.html。
 */
function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var tabName = data.__tab || '報名';
    delete data.__tab;

    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName(tabName) || ss.insertSheet(tabName);

    var keys = Object.keys(data);
    var lastCol = sheet.getLastColumn();
    var headers = lastCol > 0
      ? sheet.getRange(1, 1, 1, lastCol).getValues()[0].map(String)
      : [];

    if (headers.length === 0) {
      headers = keys;
      sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    } else {
      keys.forEach(function (k) {
        if (headers.indexOf(k) === -1) {
          headers.push(k);
          sheet.getRange(1, headers.length).setValue(k);
        }
      });
    }

    var row = headers.map(function (h) {
      return data.hasOwnProperty(h) ? data[h] : '';
    });
    sheet.appendRow(row);

    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

function doGet() {
  return json_({ ok: true, service: 'ruyi-enroll' });
}

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
