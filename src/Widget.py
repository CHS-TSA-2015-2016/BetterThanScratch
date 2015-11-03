import BasicObject;
import Rectangle

"""
    A dictionary of possible types of widgets
"""
WIDGET_TYPES = {
    "Panel": 0,
    "Canvas": 1,
    "Image": 2,
    "Label": 3,
    "Single-Line-Input": 4,
    "Multi-Line-Input": 5,
    "CheckBox": 6,
    "Button": 7,
    "Radio-Group": 8,
    "Radio-Button": 9,
    "Menu-Bar": 10,
    "Menu-Group": 11,
    "Menu-Option": 12,
    "Tree-View": 13,
    "Tree-View-Group": 14,
    "Tree-View-Item": 15,
    "Scroll-Pane": 16,
    "Slider": 17,
    "View": 18,
    "Tab-Pane": 19,
    "Tab": 20,
    "Window": 21,
    "Custom": 22
};

"""
    A dictionary that keeps track of how many of each widget are existing in the entire project
"""
WidgetCount = {
    "Panel": 0,
    "Canvas": 0,
    "Image": 0,
    "Label": 0,
    "Single-Line-Input": 0,
    "Multi-Line-Input": 0,
    "CheckBox": 0,
    "Button": 0,
    "Radio-Group": 0,
    "Radio-Button": 0,
    "Menu-Bar": 0,
    "Menu-Group": 0,
    "Menu-Option": 0,
    "Tree-View": 0,
    "Tree-View-Group": 0,
    "Tree-View-Item": 0,
    "Scroll-Pane": 0,
    "Slider": 0,
    "View": 0,
    "Tab-Pane": 0,
    "Tab": 0,
    "Window": 0,
    "Custom": 0
};

class WidgetManager(object):
    def __init__(self, widgets=[]):
        self.widgets = widgets;
        self.doomedWidgets = [];

    def addWidget(self, widget):
        self.widgets.append(widget);

    def updateWidgets(self):
        for widget in self.widgets:
            widget.update();

    def cleanWidgets(self):
        for index in range(len(self.doomedWidgets)):
            self.doomedWidets.pop();

    def update(self):
        self.updateWidgets();
        self.cleanWidets();

class Panel(BasicObject):
    def __init__(self, wm, rect, widgets=[]):
        self.x, self.y = rect.getPosition();
        self.width, self.height = rect.getSize();
        self.widgets = widgets;
        self.widgetKey = "Panel";
        self.widgetManager = wm;
        self.widgetManager.addWidget(self);

    def __str__(self):
        widetStrings = [];
        for widget in self.widgets:
            widgetStrings.append(widget.__str__());
        representation = "{ Panel<x=%s y=%s, width=%s, height=%s> << Bound Widgets: [%s]}" % (self.x, self.y, self.width, self.height, widgetStrings.join("|"));

    def addWidget(self, widget):
        self.widgets.append(widget);

    def removeWidgetByWidget(self, widget):
        for index in range(len(self.widgets)):
            if widget == self.widgets[index]:
                break;
        self.widgets[index].destroy();
        self.widgets.pop();

    def create(self):
        WidgetCount[self.widgetKey] += 1;

        for widget in self.widgets:
            widget.create();

    def update(self):
        for widget in self.widgets:
            widget.update();

    def destroy(self):
        for widget in self.widgets:
            widget.destroy();

        for index in range(len(self.widgets)):
            self.widgets.pop(index);
        self.widgetManager.doomedWidgets.append(self);

r = Rectangle(10, 10, 300, 300);
wm = WidgetManager();
p = Panel(wm, r);
print p;
input("...");
