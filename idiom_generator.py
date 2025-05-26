import random

def create_idiom(num_chars, char_list_file="kanji_list.txt"):
    """
    指定された文字数の熟語を、漢字リストファイルからランダムに生成します。

    Args:
        num_chars (int): 生成する熟語の文字数。
        char_list_file (str): 漢字リストが記載されたテキストファイルのパス。

    Returns:
        str: 生成された熟語。漢字リストが空の場合やファイルの読み込みに失敗した場合は空文字列を返します。
    """
    try:
        with open(char_list_file, "r", encoding="utf-8") as f:
            kanji_list = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"エラー: ファイル '{char_list_file}' が見つかりません。")
        return ""
    except Exception as e:
        print(f"エラー: ファイルの読み込み中にエラーが発生しました: {e}")
        return ""

    if not kanji_list:
        print("エラー: 漢字リストが空です。")
        return ""

    if num_chars > len(kanji_list):
        print("エラー: 指定された文字数が漢字リストの数を超えています。")
        return ""

    selected_chars = random.sample(kanji_list, num_chars)
    idiom = "".join(selected_chars)
    return idiom

if __name__ == "__main__":
    while True:
        try:
            num = int(input("生成する熟語の文字数を入力してください (終了は0): "))
            if num == 0:
                break
            elif num < 1:
                print("1以上の文字数を入力してください。")
                continue

            idiom = create_idiom(num)
            if idiom:
                print(f"{num}字熟語: {idiom}")

        except ValueError:
            print("数値を入力してください。")