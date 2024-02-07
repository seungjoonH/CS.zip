#include <iostream>
#include <string>

using namespace std;

struct node {
    string data;
    node* next_node;
};

class Stack {
private:
    node* head;
    node* tail;

public:
    Stack();
    void push(string str);
    bool pop();
    void display();
};

Stack::Stack() {
    head = NULL;
    tail = NULL;
}

void Stack::push(string str) {
    node* new_node = new node;
    new_node->data = str;
    new_node->next_node = head;
    head = new_node;

    if(tail == NULL)
        tail = new_node;
}

bool Stack::pop() {
    if(head == NULL) {
        cout << "No data in Stack!\n";
        return false;
    } else {
        node* temp_node = head;
        head = head->next_node;
        delete temp_node;
        
        if(head == NULL)
            tail = NULL;
    }
    return true;
}

void Stack::display() {
    if(head == NULL) {
        cout << "No data in my Stack!\n";
    } else {
        cout << "----\n";
        node* prv_node = head;
        while(prv_node != NULL) {
            cout << prv_node->data << "\n";
            prv_node = prv_node->next_node;
        }
        cout << "----\n";
    }
}

int main() {
    Stack tStack;

    while(true) {
        bool check = true;

        cout << "\n=== Linked List Tester ===\n" 
        << "(1) Push\n"
        << "(2) Pop node\n"
        << "(3) Display node\n"
        << "(0) Exit\n"
        << "==========================\n";

        int selectNum = 0;
        cout << "\nSelect your action: ";
        cin >> selectNum;
        cout << "\n";

        if(selectNum == 1) {
            string data = "";
            cout << "Add data? -> ";
            cin >> data;
            tStack.push(data);
            cout << "\nPush Completed!\n";
        } else if(selectNum == 2) {
            check = tStack.pop();
            if(check)
                cout << "\nPop Completed!\n";
            else
                cout << "\nPop Failed!\n";
        } else if(selectNum == 3) {
            cout << "++ My Stack Data ++\n";          
            tStack.display();
        } else {
            cout << "Tester Shut down! Bye ~\n\n";
            break;
        }
    }
}