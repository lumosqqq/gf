package com.fzu.dblab.ussc.cube;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class cube {
    private String [][] dataSet;
    private ArrayList<String>  dimension;
    private ArrayList<String>  inputdata;
    private ArrayList<String> removedata;
    private int minSup;

    public cube(int rank, int col,String filename) {
        this.dataSet = new String[rank][col];
        this.dimension = new ArrayList<String>();
        this.inputdata = new ArrayList<String>();
        this.removedata = new ArrayList<String>();
        this.minSup = 3;
        this.readFile(filename);
        for(int i=0;i<col;i++) {
        	 this.dimension.add(" ");
        }
        this.getOutput(0);
    }
    //读取csv数据到dataSet里面
    public void readFile(String filename){
        File inFile = new File(filename); // 读取的CSV文件
        String inString = "";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(inFile));
            inString = reader.readLine();
            String [] tempRank = null;
            for(int i=0;inString!=null;i++){
                tempRank = inString.split(",");
                for(int j=0;j<tempRank.length;j++){
                    this.dataSet[i][j] = tempRank[j];
                }
                inString=reader.readLine();
            }
            reader.close();
        } catch (FileNotFoundException ex) {
            System.out.println("file not found");
        } catch (IOException ex) {
            System.out.println("error in reading or writing");
        }
    }


    //获取数据有几个维度(维度为1时）
    public ArrayList<String> getDimension(ArrayList<String> a){
        for(int i=0;i<this.dataSet.length;i++){
            for(int j=0;j<this.dataSet[i].length;j++){
                if(check(this.dataSet[i][j],a)){
                    a.add(this.dataSet[i][j]);
                }
            }
        }
        return a;
    }

    //获取数据有几个维度(维度不为1时）
    public ArrayList<String> getDimension(ArrayList<String> a,Integer k){
        if(k>this.dataSet[0].length){
            return null;
        }else {
            for(int i=0;i<this.dataSet.length;i++){
                for(int j=0;j<=this.dataSet[i].length-k;j++){
                    String tmp = "";
                    for(int m=j;m<j+k;m++){
                        tmp = tmp + this.dataSet[i][m];
                    }
                    if(check(tmp,a)){
                        a.add(tmp);
                    }
                }
            }
        }
        for(int i=0;i<a.size();i++){
            for(int j=0;j<this.removedata.size();j++){
                if(a.get(i).contains(this.removedata.get(j))){
                    a.set(i,"");
                }
            }
        }
        ArrayList<String> endSet = new ArrayList<String>();
        for(int i=0;i<a.size();i++){
            if(a.get(i).equals("")){
                continue;
            }
            endSet.add(a.get(i));
        }
        a = endSet;
        return a;
    }
    //查看是否重复
    public boolean check(String index,ArrayList<String> t){
        boolean flag = true;
        for(int i=0;i<t.size();i++){
            if(t.get(i).equals(index)){
                flag = false;
                break;
            }
        }
        return flag;
    }
    //查看是否重复
    public boolean check(String index){
        boolean flag = true;
        for(int i=0;i<this.dimension.size();i++){
            if(String.valueOf(this.dimension.get(i).charAt(0)).equals(index)){
                flag = false;
                break;
            }
        }
        return flag;
    }

    public void getProcess(int dim){
        if(dim==1){
            ArrayList<String> tempSet = new ArrayList<String>();
            this.getDimension(tempSet);
            Integer [] SetCount = new Integer[tempSet.size()];
            for(int i=0;i<this.dataSet.length;i++){
                for(int j=0;j<this.dataSet[i].length;j++){
                    for(int k=0;k<tempSet.size();k++){
                        if(tempSet.get(k).equals(this.dataSet[i][j])){
                            if(SetCount[k]==null){
                                SetCount[k]=1;
                            }else {
                                SetCount[k] = SetCount[k] + 1;
                            }
                        }
                    }
                }
            }
            for(int i=0;i<SetCount.length;i++){
                if(SetCount[i]>=this.minSup){
                    this.inputdata.add(tempSet.get(i)+"<"+SetCount[i]+">");
                }else {
                    this.removedata.add(tempSet.get(i));
                }
            }
        }else {
            ArrayList<String> tempSet = new ArrayList<String>();
            tempSet = this.getDimension(tempSet,dim);
            this.removedata = new ArrayList<String>();
            Integer [] SetCount = new Integer[tempSet.size()];
            for(int i=0;i<this.dataSet.length;i++){
                for(int j=0;j<=this.dataSet[i].length-dim;j++){
                    String tmp = "";
                    for(int m=j;m<j+dim;m++){
                        tmp = tmp + this.dataSet[i][m];
                    }
                    for(int k=0;k<tempSet.size();k++){
                        if(tempSet.get(k).equals(tmp)){
                            if(SetCount[k]==null){
                                SetCount[k]=1;
                            }else {
                                SetCount[k] = SetCount[k] + 1;
                            }
                        }
                    }
                }
            }
            for(int i=0;i<SetCount.length;i++){
                if(SetCount[i]>=this.minSup){
                    this.inputdata.add(tempSet.get(i)+"<"+SetCount[i]+">");
                }else {
                    this.removedata.add(tempSet.get(i));
                }
            }
        }
    }
    //工作函数
    public void getOutput(int dim){
        if(dim<this.dimension.size()){
            dim = dim + 1;
            this.getProcess(dim);
            getOutput(dim);
        }
        
    }
    public static void main(String[] args){
        cube cube1 = new cube(8,4,"E:\\BUC数据集.csv");
        System.out.println("输出结果为:"+cube1.inputdata.toString());
    }
}
