package snake;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.util.*;

import javax.swing.JOptionPane;

class LocXY {

    public int x;
    public int y;

    LocXY(int xx, int yy) {
        x = xx;
        y = yy;
    }
}

/**
 * This applet uses a Timer object to animate a bouncing ball.
 */
public class Snake extends JFrame implements KeyListener {

    private int x = 50;         // Ball's X coordinate
    private int y = 100;               // Ball's Y coordinate
    private final int WIDTH = 10;      // Ball's width
    private final int HEIGHT = 10;     // Ball's height
    private final int TIME_DELAY = 100; // Time delay
    private final int MAXIMUM_Y = 400; // Min height of ball
    private final int MAXIMUM_X = 500;
    private javax.swing.Timer timer;    // Timer object
    private boolean goingUp = false;    // Direction indicator
    private boolean goingLeft = false;
    private boolean goingRight = true;
    private boolean goingDown = false;
    private Random generator;
    private Queue<LocXY> snakePositions;
    private Queue<LocXY> bugsLocations;

    public Snake() {
        timer = new javax.swing.Timer(TIME_DELAY, new TimerListener());
        timer.start();
        generator = new Random();
        addKeyListener(this);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(MAXIMUM_X + 2, MAXIMUM_Y + 2);
        setVisible(true);

        bugsLocations = new LinkedList<LocXY>();
        for (int i = 0; i < 4; i++) {
            bugsLocations.add(new LocXY ( generator.nextInt(MAXIMUM_X / WIDTH) * WIDTH,
                generator.nextInt(MAXIMUM_Y / HEIGHT) * HEIGHT));
        }
        
        snakePositions = new LinkedList<LocXY>();
        snakePositions.add(new LocXY(100, 200));
        snakePositions.add(new LocXY(150, 200));
        snakePositions.add(new LocXY(200, 200));

    }

    public void drawSnake(Graphics g)
    {
        Iterator it=snakePositions.iterator();

        g.setColor(Color.GREEN);
        while(it.hasNext())
        {
            LocXY point=(LocXY)it.next();
            g.fillRect(x, y, WIDTH, HEIGHT);
        }
    }

    public void drawBugs(Graphics g)
    {
        Iterator it=bugsLocations.iterator();

        g.setColor(Color.RED);
        while(it.hasNext())
        {
            LocXY point=(LocXY)it.next();
            g.fillRect(point.x, point.y, WIDTH, HEIGHT);
        }
    }
    
    public void paint(Graphics g) {
        // Call the superclass paint method.
        super.paint(g);

        g.setColor(Color.BLACK);
        g.drawRect(2, 2, MAXIMUM_X - 2, MAXIMUM_Y - 2);
        
        drawSnake(g);

        drawBugs(g);
    }

    /**
     * Private inner class that handles the Timer object's action events.
     *
     *
     *
     */
    private class TimerListener implements ActionListener {

        public void actionPerformed(ActionEvent e) {
            // Update the ball's Y coordinate.
            if (goingUp) {
                y -= HEIGHT;
            } else if (goingLeft) {
                x -= WIDTH;
            } else if (goingDown) {
                y += HEIGHT;
            } else if (goingRight) {
                x += WIDTH;
            }

            if ((x < 0) || (x >= MAXIMUM_X)
                    || (y < 0) || (y >= MAXIMUM_Y)) {
                System.out.println("Game over.");
                timer.stop();
            }
            
            snakePositions.add(new LocXY(x, y));
            snakePositions.remove();
            // Force a call to the paint method.
            repaint();
        }
    }

    /**
     * Handle the key typed event from the text field.
     */
    public void keyTyped(KeyEvent e) {
    }

    /**
     * Handle the key-pressed event from the text field.
     */
    public void keyPressed(KeyEvent e) {
        //displayInfo(e, "KEY PRESSED: ");
        int keyCode = e.getKeyCode();
        // System.out.println(keyCode);
        if (keyCode == KeyEvent.VK_LEFT) // Left arrow key
        {
            goingLeft = true;
            goingRight = goingUp = goingDown = false;
        }
        if (keyCode == KeyEvent.VK_RIGHT) // Left arrow key
        {
            goingRight = true;
            goingLeft = goingUp = goingDown = false;
        }
        if (keyCode == KeyEvent.VK_DOWN) // Left arrow key
        {
            goingDown = true;
            goingRight = goingUp = goingLeft = false;
        }
        if (keyCode == KeyEvent.VK_UP) // Left arrow key
        {
            goingUp = true;
            goingRight = goingLeft = goingDown = false;
        }
        repaint();
    }

    /**
     * Handle the key-released event from the text field.
     */
    public void keyReleased(KeyEvent e) {
    }

    public static void main(String[] args) {
        new Snake();
    }
}
