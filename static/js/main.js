
console.log("fjaohifoafh");

function start(save_list) {
    // 追加
    for (let i = 0; i < save_list.length; i++) {
                <!--console.log(save_list[i]) -->
                var hoge = JSON.stringify(save_list[i]);
        var pHoge = JSON.parse(hoge);

        var newElement = document.createElement("p"); // p要素作成
        var newContent = document.createTextNode("---------------------------"); // テキストノードを作成
        newElement.appendChild(newContent); // p要素にテキストノードを追加
        newElement.setAttribute("id", i); // p要素にidを設定
        var parentDiv = document.getElementById("so_far_post_id");
        // 子要素３への参照を取得
        var childP3 = document.getElementById(i);
        parentDiv.insertBefore(newElement, childP3);

        var newElement = document.createElement("p"); // p要素作成
        var newContent = document.createTextNode("投稿 " + pHoge.write_text); // テキストノードを作成
        newElement.appendChild(newContent); // p要素にテキストノードを追加
        newElement.setAttribute("id", i); // p要素にidを設定
        var parentDiv = document.getElementById("so_far_post_id");
        // 子要素３への参照を取得
        var childP1 = document.getElementById(i);
        parentDiv.insertBefore(newElement, childP1);

        var newElement = document.createElement("p"); // p要素作成
        var newContent = document.createTextNode("名前 " + pHoge.name); // テキストノードを作成
        newElement.appendChild(newContent); // p要素にテキストノードを追加
        newElement.setAttribute("id", i); // p要素にidを設定
        var parentDiv = document.getElementById("so_far_post_id");
        // 子要素３への参照を取得
        var childP2 = document.getElementById(i);
        parentDiv.insertBefore(newElement, childP2);
    }
}
