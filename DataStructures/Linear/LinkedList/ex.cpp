#include <iostream>
#include <string>

using namespace std;

struct node {
    int data;
    node* next_node;
};

class LinkedList {
private:
    node* head;
    node* tail;
public:
    LinkedList() {
        head = NULL;
        tail = NULL;
    }
    node* getHead();
    void add(int n);
    bool insert(int index, int n);
    bool pop();
    bool remove(int index);
    void display(node* head);
};

node* LinkedList::getHead() {
    return head;
}

void LinkedList::add(int n) {
    node* new_node = new node;
    new_node->data = n;

    if(head == NULL) {
        head = new_node;
        tail = new_node;
    } else {
        tail->next_node = new_node;
        tail = new_node;
    }
}

bool LinkedList::insert(int index, int n) {
    node* new_node = new node;
    new_node->data = n;

    if(index == 0) {
        new_node->next_node = head;
        head = new_node;
        if(tail == NULL) {
            tail = new_node;
        } 
     } else {
        node* cur_node = head;
        for(int i = 0; i < index - 1; i++) {
            if(cur_node == NULL) {
                cout << "\nTry another index (out of range)\n";
                delete new_node;
                return false;
            }
            cur_node = cur_node->next_node;
        }
        new_node->next_node = cur_node->next_node;
        cur_node->next_node = new_node;
        if(new_node->next_node == NULL) 
            tail = new_node;
    }
    return true;
}

bool LinkedList::pop() {
    if(head == NULL) {
        cout << "\nLinkedList is empty\n";
        return false;
    } else if(head == tail) {
        delete tail;
        head = tail = NULL;
    } else {
        node* prv_node = head;
        while(prv_node->next_node != tail) {
            prv_node = prv_node->next_node;
        }
        delete tail;
        tail = prv_node;
        tail->next_node = NULL;
    }
    return true;
}

bool LinkedList::remove(int index) {
    if(head == NULL) {
        cout << "LinkedList is empty\n";
        return false;
     } else if(index == 0) {
        node* temp_node = head->next_node;
        delete head;
        head = temp_node;

        if(head == NULL)
            tail = NULL;
     } else {
        node* cur_node = head;
        for(int i = 0; i < index - 1; i++) {
            if(cur_node == NULL) {
                cout << "\nTry another index (out of range)\n";
                return false;
            }
            cur_node = cur_node->next_node;
        }
        node* temp_node = cur_node->next_node;
        cur_node->next_node = temp_node->next_node;
        delete temp_node;

        if(temp_node->next_node == NULL) 
            tail = temp_node;
    }
    return true;
}

void LinkedList::display(node* head) {
    
    if(head == NULL)
        cout << "]\n";
    else {
        cout << head->data << ", ";
        display(head->next_node);
    }
}

int main() {
    LinkedList lList;

    while(true) {
        bool check = true;

        cout << "\n=== Linked List Tester ===\n" 
        << "(1) Add node\n"
        << "(2) Insert node\n"
        << "(3) Pop node\n"
        << "(4) Remove node\n"
        << "(5) Display node\n"
        << "(0) Exit\n"
        << "==========================\n";

        int selectNum = 0;
        cout << "\nSelect your action: ";
        cin >> selectNum;
        cout << "\n";

        if(selectNum == 1) {
            int num = 0;
            cout << "Add num? -> ";
            cin >> num;
            
            lList.add(num);
            cout << "\nAdd Completed!\n";
        } else if(selectNum == 2) {
            int index = 0, num = 0;
            cout << "\nIndex? -> ";
            cin >> index;
            cout << "Add num? -> ";
            cin >> num;

            check = lList.insert(index, num);
            if(check)
                cout << "\nInsert Completed!\n";
            else
                cout << "\nInsert Failed!\n";
        } else if(selectNum == 3) {
            check = lList.pop();
            if(check)
                cout << "\nPop Completed!\n";
            else
                cout << "\nPop Failed!\n";
        } else if(selectNum == 4) {
            int index = 0;
            cout << "\nIndex? -> ";
            cin >> index;

            check = lList.remove(index);
            if(check)
                cout << "\nRemove Completed!\n";
            else
                cout << "\nRemove Failed!\n";
        } else if(selectNum == 5) {
            cout << "++ My Linked List Data ++\n" << "[ ";
            
            lList.display(lList.getHead());
        } else {
            cout << "Tester Shut down! Bye ~\n\n";
            break;
        }
    }
}