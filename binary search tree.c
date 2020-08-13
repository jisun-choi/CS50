//이진 검색 트리의 노드 구조
typedef struct node
{   //노드 값
    int number;
    //왼쪽 자식 노드
    struct node *left;
    //오른쪽 자식 노드
    struct node *right;
}
node;

//이진 검색 함수(*tree는 이진 검색 트리를 가리키는 포인터)
bool search(node *tree)
{   //트리가 비어있으면 false 반환 후 종료
    if(tree == NULL)
    {
        return false;
    }
    //현재 노드 값이 50보다 크면 왼쪽 노트 검색
    else if (50 < tree->number)
    {
        return search(tree->left);
    }
    //현재 노드 값이 50보다 작으면 오른쪽 노트 검색
    else if (50 > tree->number)
    {
        return search(tree->right);
    }
    else
    {
        return true;
    }
}