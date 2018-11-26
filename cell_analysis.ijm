// open("/Users/kushagrasharma/Downloads/10162017_DIFFNEURO_DOX-0829_DIV24_SYN_PSD95/10162017_DIFFNEURO_DOX-0829_DIV24_SAMPLE-A_SYN_PSD95_1Z.oib");

run("Duplicate...", "duplicate");
setAutoThreshold("Default dark no-reset");
//run("Threshold...");
setOption("BlackBackground", true);
run("Convert to Mask", "method=Default background=Dark calculate black");
run("Close");
run("Close-", "stack");
run("Set Measurements...", "area mean min display redirect=10162017_DIFFNEURO_DOX-0829_DIV24_SAMPLE-A_SYN_PSD95_1Z.oib decimal=3");
run("Analyze Particles...", "size=2-Infinity circularity=0.15-1.00 display clear stack");
saveAs("Results", "/Users/kushagrasharma/Downloads/10162017_DIFFNEURO_DOX-0829_DIV24_SYN_PSD95/Results_1.csv");
MY MACRO

filename = getArgument;
if (filename=="") exit ("No argument!"); 
counter = 0;
function runAnalysis(img) {
        run("Duplicate...", "duplicate")
        selectWindow(title);
        close();
        counter++;
}