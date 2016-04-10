package com.xkcd.iresq;

import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.util.Log;

import com.estimote.sdk.Beacon;
import com.estimote.sdk.BeaconManager;
import com.estimote.sdk.Region;
import com.estimote.sdk.SystemRequirementsChecker;
import com.estimote.sdk.Utils;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

/**
 * Created by laksh on 10/4/16.
 */
public abstract class BaseDemoActivity extends FragmentActivity implements OnMapReadyCallback {

    protected GoogleMap mMap;
    protected Region region;
    protected BeaconManager beaconManager;
    protected  List<Beacon> mBeacons;
    protected int getLayoutId() {
        return R.layout.map;
    }

    public static double my_lat = 28.6091309;
    public static double my_long = 77.0328799;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(getLayoutId());
        setUpMap();

        beaconManager = new BeaconManager(this);
        region = new Region("ranged region",
                UUID.fromString("B9407F30-F5F8-466E-AFF9-25556B57FE6D"), null, null);
        beaconManager.setRangingListener(new BeaconManager.RangingListener() {
            @Override
            public void onBeaconsDiscovered(Region region, final List<Beacon> rangedBeacons) {
                // Note that results are not delivered on UI thread.
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        ArrayList<LatLng> list = new ArrayList<LatLng>();
                        for (Beacon rangedBeacon : rangedBeacons) {
                            Log.d("[beacon]", "Rssi" + rangedBeacon.getRssi());
                            Log.d("[beacon]", "Mac" + rangedBeacon.getMacAddress());
                            Log.d("[beacon]", "Distance" + Math.min(Utils.computeAccuracy(rangedBeacon), 6.0));
                            double distance = Utils.computeAccuracy(rangedBeacon) / 1000;
                            double lat = my_lat + distance / 110.574;
                            double lng = my_long + distance / 111.321;
                            list.add(new LatLng(lat, lng));
                            redraw(new DataSet(list));
                            Log.e("[beacon-e]", lat + "; " + lng);
                        }
                    }
                });
            }
        });
    }

    @Override
    protected void onPause() {
        beaconManager.stopRanging(region);

        super.onPause();
    }

    @Override
    protected void onResume() {
        super.onResume();
        setUpMap();

        SystemRequirementsChecker.checkWithDefaultDialogs(this);

        beaconManager.connect(new BeaconManager.ServiceReadyCallback() {
            @Override
            public void onServiceReady() {
                beaconManager.startRanging(region);
            }
        });
    }

    @Override
    public void onMapReady(GoogleMap map) {
        if (mMap != null) {
            return;
        }
        mMap = map;
        startDemo();
    }

    private void setUpMap() {
        ((SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map)).getMapAsync(this);
    }

    /**
     * Run the demo-specific code.
     */
    protected abstract void startDemo();

    protected abstract void redraw(DataSet mDataset);

    protected GoogleMap getMap() {
        return mMap;
    }
}
