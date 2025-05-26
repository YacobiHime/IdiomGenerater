import random

def create_idiom(num_chars):
    kanji_list = []
    # ファイルから漢字を読み込む+エラーの処理
    try:
        with open("kanji_list.txt", "r", encoding="utf-8") as file:
            for line in file: # 行ごとに値を入れていく
                kanji_list.append(line.strip()) # strip()で改行を削除し、リストに追加
    
    except FileNotFoundError:
        print("Error: 「kanji_list.txt」が見つかりません")
        return None
    except Exception as e:
        print(f"Error: ファイルの読み込み中に問題が発生しました:{e}")
        return None

    if not kanji_list:
        print("Error: 漢字リストが空です")
        return None
    
    # ここからは指定された文字数の漢字をランダムに選択して熟語を生成
    if num_chars > len(kanji_list):
        print(f"Error: 指定された文字数（{num_chars}）は、漢字リストの数（{len(kanji_list)}）より多いです。")
        print("リストに漢字を追加するか、より少ない文字数を指定してください。")
        return None
    
    # print(kanji_list) # デバッグ用
    selected_chars = random.sample(kanji_list, num_chars) # num_chars個の漢字をランダムに選択
    
    idiom = "".join(selected_chars) # 選択した漢字を結合して熟語を作成
    return idiom

# メイン処理
if __name__ == "__main__": 
    while True:
        try:
            num = int(input("生成する熟語の文字数を入力してください（終了する場合は0を入力）>>>"))
            
            if num == 0:
                print("プログラムを終了します。")
                break
            elif num < 1:
                print("Error: 1以上の整数を入力してください。")
                continue
            
            idiom_result = create_idiom(num) # 熟語を生成

            # 結果の表示
            if idiom_result:
                print(f"{num}字熟語: {idiom_result}")

                
        except ValueError:
            print("Error: 有効な整数を入力してください。")
        
        except Exception as e:
            print(f"Error: 予期しないエラーが発生しました: {e}")