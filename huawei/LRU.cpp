#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<map>
using namespace std;

struct CacheNode {//�����ڵ�
	int key;//��
	int value;//ֵ
	CacheNode* pre, * next;//�ڵ�ǰ�����ָ��
	CacheNode(int k, int v) : key(k), value(v), pre(NULL), next(NULL) {}
};
class LRUCache {
private:
    int size;           //����       
    CacheNode* head, * tail;//��ͷ��β
    map<int, CacheNode*> mp;          // hash��
public:
    LRUCache(int capacity)//��ʼ��
    {
        size = capacity;
        head = NULL;
        tail = NULL;
    }

    int get(int key)//���key��hashmap�д��ڣ���Ѷ�Ӧ�Ľڵ�ŵ�����ͷ���������ض�Ӧ��valueֵ����������ڣ��򷵻�-1��
    {
        map<int, CacheNode*>::iterator tar = mp.find(key);//map�ҵ�key
        if (tar != mp.end())
        {
            CacheNode* node = tar->second;//ָ����һ��
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
     //�ڵ���ڣ�ɾ���ýڵ㣬���Ƶ����µģ������ڣ�������������һ����ȥ���ټӣ���û������λ�ڼӽ�ȥ

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

    void remove(CacheNode* node)//�Ƴ�
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