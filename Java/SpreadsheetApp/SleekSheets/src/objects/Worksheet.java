package objects;

import java.util.HashMap;

public class Worksheet {
    String title;
    
    HashMap<String, Cell> cells = new HashMap<String, Cell>();

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public HashMap<String, Cell> getCells() {
        return cells;
    }

    public void setCells(HashMap<String, Cell> cells) {
        this.cells = cells;
    }
}
