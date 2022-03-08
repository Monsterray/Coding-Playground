package importers;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;

import objects.Cell;
import objects.Worksheet;

public class csvImporter implements Importer{

    @Override
    public Worksheet importToSleek(File toImport){
        Worksheet tempSheet = new Worksheet();

        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(toImport));
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        try {
            char column = 'A';
            for (String line = br.readLine(); line != null; line = br.readLine()) {
                String[] result = line.split(",");
                int row = 1;
                for(String s : result){
                    String location = new StringBuilder().append(column).append(row).toString();
                    Cell importedCell = new Cell(location, s);
                    tempSheet.getCells().put(location, importedCell);
                    row++;
                }
            }
        } catch (Exception e) {
            //TODO: handle exception
        }
        
        return tempSheet;
    }

}
