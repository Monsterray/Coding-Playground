package objects;

public class CellFormating {

    private static final String[] DEFAULT_BOARDERS = {"no","no","no","no"};
    String backgroundColor = "black";
    String foregroundColor = "lightGrey";
    double fontSize = 11;
    /**
     *  Options are; no, dotted, dashed, solid
     *  
     *  <br><br>You can add -solid or -thin to make boarders as stated.
     */
    String[] boarders = DEFAULT_BOARDERS;

}
