package importers;

import java.io.File;

import objects.Worksheet;

public interface Importer {
    /**
     *   Return: True if successful import
     */
    public Worksheet importToSleek(File toImport);

}
