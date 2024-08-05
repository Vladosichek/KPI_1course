#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include <QLineEdit>
#include <QTextEdit>
#include <QLabel>

class MainWindow : public QMainWindow
{
    Q_OBJECT
public:

    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
private slots:
    void addButton();
    void retireButton();
    void raiseButton();
    void lowerButton();
    void allButton();
    void actualButton();
    void unactualButton();
private:
    QTextEdit *outputField;
    QLineEdit *inputCode;
    QLineEdit *inputName;
    QLineEdit *inputSalary;
    QLineEdit *inputDuties;
    QLineEdit *inputRequirements;
    QLineEdit *inputPosition;
    QLineEdit *inputAmount;
};
#endif // MAINWINDOW_H
