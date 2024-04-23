// console log

Debug.Log("hello");

// 変数と定数
string say = "hello world";
Debug.Log(say);

const string say2 = "hello world 2";
Debug.Log(say2);


// 変数の型
// 文字列型
string name = "Yuki";
int hp = 100;
float speed = 158.9f;
bool flag1 = true;

// 演算
// + - * / % += -+ ++ -- , bool(&& || !)

// 文字列の連結 
// string.Format()
const string name = "Yuki";
int hp = 98;
Debug.Log(string.Format("{0}のHP: {1}", name, hp));

// if
// if, else if, else

// switch
string characterType = "Player";
switch (characterType)
{
    case "Player":
    case "Friend":
        Debug.Log("Ally");
        break;
    default:
        break;
}

// while, for
int x = 0;
while (x < 10)
{
    Debug.Log(x);
    x++;

    if (x == 7) break;
}
for (int i = 0; i < 10; i++)
{
    Debug.Log(i);
}
for (int i = 0; i <= 20; i++)
{
    if (i % 2 == 0) Debug.Log(i);
}


// 列挙型
// 制限を作って使用するためのもの
enum DIRECTION
{
    STOP,
    RIGHT,
    LEFT,
    TOP,
    BOTTOM
}

DIRECTION direction; // 宣言
direction = DIRECTION.STOP;
Debug.Log((int)direction); // intにもできる

enum PLAYER_TYPE
{
    ENEMY,
    USER
}
[SerializeField] PLAYER_TYPE playerType; // UnityのInspectorで設定できるようになる


// 配列
// pattern1
int[] xList = new int[3];
xList[0] = 0;
xList[1] = 1;
xList[2] = 9;

// pattern2 
int[] vList = new int[3] { 0, 2, -3 };

Debug.Log(vList[0]);
Debug.Log(vList.Length);

int[] arr = new int[31];
for (int i = 0; i < arr.Length; i++)
{
    arr[i] = i;
}
Debug.Log(arr.Length);

// List
// Listは配列とほぼ同じだが、追加削除ができる（メソッドがある）
List<int> numbers = new List<int>() { -1, 2, 23 };
numbers[1] = 33;
numbers.Add(100);

Debug.Log(numbers.Count);

numbers.RemoveAt(1); // index
numbers.Remove(-1); // the value itself
Debug.Log(numbers.Count);

List<int> nums = new List<int>();
for (int i = 1; i <= 10; i++)
{
    nums.Add(i);
}
Debug.Log(nums.Count);

// foreach 配列とListで使える
foreach (int item in nums)
{
    Debug.Log(item);
}

// 関数
string SampleNameFunction(string sampleName)
{
    Debug.Log(sampleName);
    return sampleName + "san";
}

List<int> GetThreeAhoNumberList(int a, int b)
{
    List<int> nums = new List<int>();
    for (int i = a; i <= b; i++)
    {
        if (IsThreeNumber(i)) nums.Add(i);
    }

    bool IsThreeNumber(int number)
    {
        if (number % 3 == 0) return true;
        while (number != 0)
        {
            if (number % 10 == 3) return true; // 一桁目が3の倍数かどうか
            number /= 10; // 上がfalseの時、その桁を消して次を確認
        }

        return false;
    }
    return nums;
}

// class
public class PlayerModel
{
    // 変数には原則public化はしない, propertyを使う
    string name;
    int hp;
    int at;

    // property
    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    // 生成された時に呼び出される
    public PlayerModel(string name)
    {
        this.name = name;
    }

    public void SayName()
    {
        Debug.Log(name);
    }
}


PlayerModel player = new PlayerModel("Hoooo");
player.SayName();
Debug.Log(player.name);