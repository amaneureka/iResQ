package com.xkcd.iresq;

import com.google.android.gms.maps.model.LatLng;

import java.util.ArrayList;

/**
 * Created by amaneureka on 10-04-2016.
 */
class DataSet {
    private ArrayList<LatLng> mDataset;
    private String mUrl;

    public DataSet(ArrayList<LatLng> dataSet) {
        this.mDataset = dataSet;
        this.mUrl = "";
    }

    public DataSet(ArrayList<LatLng> dataSet, String url) {
        this.mDataset = dataSet;
        this.mUrl = url;
    }

    public ArrayList<LatLng> getData() {
        return mDataset;
    }

    public String getUrl() {
        return mUrl;
    }
}

