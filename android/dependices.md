dependencies {
  // Debug builds: LeakCanary with internal viewer
  debugImplementation 'com.squareup.leakcanary:leakcanary-android:2.X.X'

  // Release builds: LeakCanary without internal viewer
  releaseImplementation 'com.squareup.leakcanary:leakcanary-object-watcher-android:2.X.X'
}