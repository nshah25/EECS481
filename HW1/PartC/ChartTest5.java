/* Adapted From 
 * 
 * https://github.com/jfree/jfree-demos/blob/master/src/main/java/org/jfree/chart/demo/PieChartDemo1.java
 *
 * and
 *
 * http://www.jfree.org/phpBB2/viewtopic.php?f=3&t=25969
 */
/* ----------------------------
* LegendTitleToImageDemo2.java
* ----------------------------
* (C) Copyright 2008, by Object Refinery Limited.
*
*/

package test;

import java.awt.Color;
import java.awt.Font;
import java.awt.geom.Point2D;
import java.awt.geom.Rectangle2D;
import java.awt.GradientPaint;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.awt.Point;
import java.awt.RadialGradientPaint;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import org.jfree.chart.block.RectangleConstraint;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtils;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PiePlot;
import org.jfree.chart.plot.PiePlot3D; 

import org.jfree.chart.title.LegendTitle;
import org.jfree.chart.title.TextTitle;
import org.jfree.chart.ui.ApplicationFrame;
import org.jfree.chart.ui.HorizontalAlignment;
import org.jfree.chart.ui.RectangleEdge;
import org.jfree.chart.ui.RectangleInsets;
import org.jfree.chart.ui.UIUtils;
import org.jfree.data.general.DefaultPieDataset;
import org.jfree.data.general.PieDataset;
import org.jfree.chart.ChartFactory; 
import org.jfree.data.*;
import org.jfree.chart.*;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.CategoryDataset; 
import org.jfree.data.category.DefaultCategoryDataset; 



import org.jfree.data.Range;

/**
* Here we save a legend to a PNG file...the legend has a lot of items, so we
* apply a width constraint so it doesn't get too wide.
*/
public class ChartTest5 {

    private static CategoryDataset createDataset( ) {
      final String fiat = "FIAT";        
      final String audi = "AUDI";        
      final String ford = "FORD";        
      final String speed = "Speed";        
      final String millage = "Millage";        
      final String userrating = "User Rating";        
      final String safety = "safety";        
      final DefaultCategoryDataset dataset = 
      new DefaultCategoryDataset( );  

      dataset.addValue( 1.0 , fiat , speed );        
      dataset.addValue( 3.0 , fiat , userrating );        
      dataset.addValue( 5.0 , fiat , millage ); 
      dataset.addValue( 5.0 , fiat , safety );           

      dataset.addValue( 5.0 , audi , speed );        
      dataset.addValue( 6.0 , audi , userrating );       
      dataset.addValue( 10.0 , audi , millage );        
      dataset.addValue( 4.0 , audi , safety );

      dataset.addValue( 4.0 , ford , speed );        
      dataset.addValue( 2.0 , ford , userrating );        
      dataset.addValue( 3.0 , ford , millage );        
      dataset.addValue( 6.0 , ford , safety );               

      return dataset; 
   }

    private static JFreeChart createBarChart(CategoryDataset dataset) {
        return ChartFactory.createBarChart("Bar Chart", "Domain", "Range", 
                dataset, PlotOrientation.HORIZONTAL, true, true, true);
    }
    // private static JFreeChart createBarChart3D(CategoryDataset dataset) {
    //     return ChartFactory.createBarChart3D("Bar Chart", "Domain", "Range", 
    //             dataset, PlotOrientation.HORIZONTAL, true, true, true);
    // }
    private static JFreeChart createLineChart(CategoryDataset dataset) {
        return ChartFactory.createLineChart("Bar Chart", "Domain", "Range", 
                dataset, PlotOrientation.HORIZONTAL, true, true, true);
    }
    // private static JFreeChart createLineChart3D(CategoryDataset dataset) {
    //     return ChartFactory.createLineChart3D("Bar Chart", "Domain", "Range", 
    //             dataset, PlotOrientation.HORIZONTAL, true, true, true);
    // }

    /**
     * Entry point.
     *
     * @param args  command line arguments (ignored).
     *
     * @throws IOException if there is an input/output problem.
     */
    public static void main(String[] args) throws IOException {
        // PieDataset dataset = createDataset();
        CategoryDataset dataset = createDataset();
        JFreeChart chart = createBarChart(dataset); 
        BufferedImage img = new BufferedImage(1, 1,
        BufferedImage.TYPE_INT_ARGB);
        Graphics2D g2 = img.createGraphics();
        g2.dispose();

        // now create an image of the required size for the legend
        int w = (int) Math.rint(800);
        int h = (int) Math.rint(600);
        BufferedImage img2 = new BufferedImage(w, h,
                BufferedImage.TYPE_INT_ARGB);
        Graphics2D g22 = img2.createGraphics();
        chart.draw(g22, new Rectangle2D.Double(0, 0, w, h));
        g22.dispose();

        // ...and save it to a PNG image
        OutputStream out = new BufferedOutputStream(new FileOutputStream(
                new File("output5.png")));
        ChartUtils.writeBufferedImageAsPNG(out, img2);
        out.close();
        System.out.println("output5.png created"); 


        // NEXT -------------------------------------

        // JFreeChart chart2 = createBarChart3D(dataset); 
        // img = new BufferedImage(1, 1,
        // BufferedImage.TYPE_INT_ARGB);
        // g2 = img.createGraphics();
        // g2.dispose();

        // // now create an image of the required size for the legend
        // w = (int) Math.rint(800);
        // h = (int) Math.rint(600);
        // img2 = new BufferedImage(w, h,
        //         BufferedImage.TYPE_INT_ARGB);
        // g22 = img2.createGraphics();
        // chart2.draw(g22, new Rectangle2D.Double(0, 0, w, h));
        // g22.dispose();

        // // ...and save it to a PNG image
        // out = new BufferedOutputStream(new FileOutputStream(
        //         new File("output6.png")));
        // ChartUtils.writeBufferedImageAsPNG(out, img2);
        // out.close();
        // System.out.println("output6.png created"); 

        // NEXT -------------------------------------

        JFreeChart chart3 = createLineChart(dataset); 
        img = new BufferedImage(1, 1,
        BufferedImage.TYPE_INT_ARGB);
        g2 = img.createGraphics();
        g2.dispose();

        // now create an image of the required size for the legend
        w = (int) Math.rint(800);
        h = (int) Math.rint(600);
        img2 = new BufferedImage(w, h,
                BufferedImage.TYPE_INT_ARGB);
        g22 = img2.createGraphics();
        chart3.draw(g22, new Rectangle2D.Double(0, 0, w, h));
        g22.dispose();

        // ...and save it to a PNG image
        out = new BufferedOutputStream(new FileOutputStream(
                new File("output7.png")));
        ChartUtils.writeBufferedImageAsPNG(out, img2);
        out.close();
        System.out.println("output7.png created"); 

        // NEXT -------------------------------------

        // JFreeChart chart4 = createLineChart3D(dataset); 
        // img = new BufferedImage(1, 1,
        // BufferedImage.TYPE_INT_ARGB);
        // g2 = img.createGraphics();
        // g2.dispose();

        // // now create an image of the required size for the legend
        // w = (int) Math.rint(800);
        // h = (int) Math.rint(600);
        // img2 = new BufferedImage(w, h,
        //         BufferedImage.TYPE_INT_ARGB);
        // g22 = img2.createGraphics();
        // chart4.draw(g22, new Rectangle2D.Double(0, 0, w, h));
        // g22.dispose();

        // // ...and save it to a PNG image
        // out = new BufferedOutputStream(new FileOutputStream(
        //         new File("output8.png")));
        // ChartUtils.writeBufferedImageAsPNG(out, img2);
        // out.close();
        // System.out.println("output8.png created"); 
    }
}
