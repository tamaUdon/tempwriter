// ref. https://qiita.com/shibaura/items/48bca63ac992c2f93b9d

if (!window.Escpos) {
    window.Escpos = {};
}

var webSocket; //ウェブソケット
var messageTextArea = document.getElementById("messageTextArea"); // HTML内のテキスト出力エリア

// サーバとの通信を接続する関数
function connect(){
    webSocket = new WebSocket("ws://localhost:8989"); // インスタンスを作り、サーバと接続

    // ソケット接続すれば呼び出す関数を設定
    webSocket.onopen = function(message){
    messageTextArea.value += "Server connect... OK\n";
    };

    // ソケット接続が切ると呼び出す関数を設定
    webSocket.onclose = function(message){
    messageTextArea.value += "Server Disconnect... OK\n";
    };

    // ソケット通信中でエラーが発生すれば呼び出す関数を設定
    webSocket.onerror = function(message){
    messageTextArea.value += "error...\n";
    };

    // ソケットサーバからメッセージが受信すれば呼び出す関数を設定
    // ここで画面上の矩形を表示on/off
    webSocket.onmessage = function(message){
    messageTextArea.value += "Receive => "+message.data+"\n";
    };
}

// サーバにメッセージを送信する関数
function sendMessage(){
    var message = document.getElementById("textMessage");
    messageTextArea.value += "Send => "+message.value+"\n";
    webSocket.send(message.value);
    message.value = "";
}

// サーバとの通信を切断する関数
function disconnect(){
    webSocket.close();
}