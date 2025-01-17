/*
 * Copyright (c) 2023 Airbyte, Inc., all rights reserved.
 */

package io.airbyte.workers.temporal.sync;

import io.temporal.activity.ActivityInterface;
import io.temporal.activity.ActivityMethod;
import java.util.UUID;

/**
 * RefreshSchemaActivity.
 */
@ActivityInterface
public interface RefreshSchemaActivity {

  @ActivityMethod
  boolean shouldRefreshSchema(UUID sourceCatalogId);

  public void refreshSchema(UUID sourceCatalogId, UUID connectionId) throws Exception;

}
