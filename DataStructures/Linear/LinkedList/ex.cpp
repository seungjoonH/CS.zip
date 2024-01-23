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
    void insert(int index, int n);
    void pop();
    void remove(int index);
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

void LinkedList::insert(int index, int n) {

}

void LinkedList::pop() {
    if(head == NULL) {
        cout << "LinkedList is empty";
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
}

void LinkedList::remove(int index) {

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
        cout << "\n=== Linked List Tester ===\n" 
        << "(1) Add node\n"
        << "(2) Insert node\n"
        << "(3) Pop node\n"
        << "(4) Remove node\n"
        << "(5) display node\n"
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
            cout << "\nAdd num? -> ";
            cin >> num;

            lList.insert(index, num);
            cout << "\nInsert Completed!\n";
        } else if(selectNum == 3) {
            lList.pop();
            cout << "\nPop Completed!\n";
        } else if(selectNum == 4) {
            int index = 0;
            cout << "\nIndex? -> ";
            cin >> index;

            lList.remove(index);
            cout << "\nPop Completed!\n";
        } else if(selectNum == 5) {
            cout << "++ My Linked List Data ++\n";
            
            lList.display(lList.getHead());
        } else {
            cout << "Tester Shut down! Bye ~\n\n";
            break;
        }
    }
}