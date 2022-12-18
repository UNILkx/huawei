#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<map>
using namespace std;

struct CacheNode {//建立节点
	int key;//键
	int value;//值
	CacheNode* pre, * next;//节点前驱后继指针
	CacheNode(int k, int v) : key(k), value(v), pre(NULL), next(NULL) {}
};
class LRUCache {
private:
    int size;           //容量       
    CacheNode* head, * tail;//表头表尾
    map<int, CacheNode*> mp;          // hash表
public:
    LRUCache(int capacity)//初始化
    {
        size = capacity;
        head = NULL;
        tail = NULL;
    }

    int get(int key)//如果key在hashmap中存在，则把对应的节点放到链表头部，并返回对应的value值；如果不存在，则返回-1。
    {
        map<int, CacheNode*>::iterator tar = mp.find(key);//map找到key
        if (tar != mp.end())
        {
            CacheNode* node = tar->second;//指向下一个
            remove(node);
            putHead(node);
            return node->value;
        }
        else
        {
            return -1;
        }
    }
    void put(int key, int value)
     //节点存在，删除该节点，并推到最新的；不存在，若已满，先推一个出去，再加；若没满，移位在加进去

    {
        map<int, CacheNode*>::iterator tar = mp.find(key);
        if (tar != mp.end())
        {
            CacheNode* node = tar->second;
            node->value = value;
            remove(node);
            putHead(node);
        }
        else
        {
            CacheNode* newNode = new CacheNode(key, value);
            if (mp.size() >= size)
            {
                map<int, CacheNode*>::iterator iter = mp.find(tail->key);
                remove(tail);
                mp.erase(iter);
            }
            putHead(newNode);
            mp[key] = newNode;
        }
    }

    void remove(CacheNode* node)//移除
    {
        if (node->pre != NULL)
        {
            node->pre->next = node->next;
        }
        else
        {
            head = node->next;
        }
        if (node->next != NULL)
        {
            node->next->pre = node->pre;
        }
        else
        {
            tail = node->pre;
        }
    }

    void putHead(CacheNode* node)
    {
        node->next = head;
        node->pre = NULL;

        if (head != NULL)
        {
            head->pre = node;
        }
        head = node;
        if (tail == NULL)
        {
            tail = head;
        }
    }
};


int main(int argc, char** argv)
{
    LRUCache* lruCache = new LRUCache(2);
    lruCache->put(2, 1);
    lruCache->put(1, 1);
    cout << lruCache->get(2) << endl;
    lruCache->put(4, 1);
    cout << lruCache->get(1) << endl;
    cout << lruCache->get(2) << endl;
}